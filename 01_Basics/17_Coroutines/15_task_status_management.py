#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：asyncio.Task 状态管理 - cancelled()、done()、result()、exception()。
Author: Lambert

本示例演示 asyncio.Task 的状态检查方法：

1. **task.done()** - 检查任务是否完成
2. **task.cancelled()** - 检查任务是否被取消
3. **task.cancel()** - 取消任务
4. **task.result()** - 获取任务结果（如果已完成）
5. **task.exception()** - 获取任务异常（如果抛出异常）

这些方法对于构建健壮的异步应用非常重要，特别是在需要：
- 检查任务执行状态
- 处理任务取消
- 获取任务结果或异常
- 实现超时和重试逻辑
"""

from __future__ import annotations

import asyncio
from typing import Any

# ExceptionGroup 是 Python 3.11+ 内置的
# Python 3.10 或更早版本需要安装 exceptiongroup 库
try:
    ExceptionGroup
except NameError:
    # Python 3.10 或更早版本
    try:
        from exceptiongroup import ExceptionGroup
    except ImportError:
        # 如果未安装，定义一个简单的替代类
        class ExceptionGroup(BaseException):
            """ExceptionGroup 的简单替代类（用于演示）。"""
            def __init__(self, message: str, exceptions: list[Exception]):
                super().__init__(message)
                self.message = message
                self.exceptions = exceptions


# =============================================================================
# Task.done() - 检查任务是否完成
# =============================================================================


async def demo_task_done() -> None:
    """示例 01：task.done() - 检查任务完成状态。"""
    print("== task.done() - 检查任务完成状态 ==\n")

    async def worker(name: str, delay: float) -> str:
        await asyncio.sleep(delay)
        return f"{name} 完成"

    # 创建任务
    task = asyncio.create_task(worker("Task-1", 0.5))

    print(f"1. 刚创建: task.done() = {task.done()}")
    await asyncio.sleep(0.2)
    print(f"2. 运行中: task.done() = {task.done()}")

    # 等待完成
    await task
    print(f"3. 完成后: task.done() = {task.done()}")
    print(f"4. 结果: task.result() = {task.result()}")


async def demo_task_done_multiple() -> None:
    """示例 02：检查多个任务的完成状态。"""
    print("\n== 检查多个任务的完成状态 ==\n")

    async def worker(id: int, delay: float) -> int:
        await asyncio.sleep(delay)
        return id * 10

    # 创建多个不同时长的任务
    tasks = [
        asyncio.create_task(worker(1, 0.3)),
        asyncio.create_task(worker(2, 0.1)),
        asyncio.create_task(worker(3, 0.5)),
        asyncio.create_task(worker(4, 0.2)),
    ]

    # 轮询检查任务完成状态
    start = asyncio.get_event_loop().time()
    while any(not t.done() for t in tasks):
        await asyncio.sleep(0.1)
        done_count = sum(1 for t in tasks if t.done())
        elapsed = asyncio.get_event_loop().time() - start
        print(f"[{elapsed:.1f}s] 已完成: {done_count}/{len(tasks)}")

    print("\n所有任务完成，获取结果:")
    for i, task in enumerate(tasks, 1):
        print(f"  Task-{i}: {task.result()}")


# =============================================================================
# Task.cancel() 和 cancelled() - 取消任务
# =============================================================================


async def demo_task_cancel() -> None:
    """示例 03：task.cancel() - 取消任务。"""
    print("\n\n== task.cancel() - 取消任务 ==\n")

    async def cancellable_worker(name: str) -> str:
        try:
            print(f"[{name}] 开始工作...")
            for i in range(5):
                await asyncio.sleep(0.2)
                print(f"[{name}] 工作进度: {i+1}/5")
            return f"{name} 完成"
        except asyncio.CancelledError:
            print(f"[{name}] 收到取消请求，清理中...")
            await asyncio.sleep(0.1)  # 模拟清理
            print(f"[{name}] 清理完成，退出")
            raise  # 必须重新抛出 CancelledError

    # 创建任务
    task = asyncio.create_task(cancellable_worker("Worker-1"))

    # 运行一段时间后取消
    await asyncio.sleep(0.5)
    print(f"\n[主控] 发起取消请求")
    task.cancel()

    # 等待任务处理取消
    try:
        await task
    except asyncio.CancelledError:
        print(f"[主控] 任务已取消")

    print(f"\n取消后状态:")
    print(f"  task.done() = {task.done()}")
    print(f"  task.cancelled() = {task.cancelled()}")


async def demo_task_cancelled() -> None:
    """示例 04：task.cancelled() - 检查任务是否被取消。"""
    print("\n== task.cancelled() - 检查取消状态 ==\n")

    async def worker(name: str) -> str:
        await asyncio.sleep(1)
        return f"{name} 完成"

    # 创建并取消任务
    task1 = asyncio.create_task(worker("Task-1"))
    task1.cancel()

    task2 = asyncio.create_task(worker("Task-2"))

    # 等待处理
    try:
        await task1
    except asyncio.CancelledError:
        pass

    await asyncio.sleep(0.1)  # task2 还在运行

    print(f"Task-1 (被取消):")
    print(f"  done() = {task1.done()}, cancelled() = {task1.cancelled()}")

    print(f"\nTask-2 (运行中):")
    print(f"  done() = {task2.done()}, cancelled() = {task2.cancelled()}")

    # 等待 task2 完成
    await task2
    print(f"\nTask-2 (完成后):")
    print(f"  done() = {task2.done()}, cancelled() = {task2.cancelled()}")


async def demo_cancel_with_timeout() -> None:
    """示例 05：使用超时自动取消任务。"""
    print("\n== 使用超时自动取消任务 ==\n")

    async def slow_worker() -> str:
        print("[Worker] 开始慢速工作...")
        await asyncio.sleep(5)  # 需要 5 秒
        return "工作完成"

    async def with_timeout_check() -> None:
        """带超时和状态检查的执行。"""
        task = asyncio.create_task(slow_worker())

        try:
            # 使用 timeout 上下文管理器
            async with asyncio.timeout(1.0):
                result = await task
                print(f"结果: {result}")
        except asyncio.TimeoutError:
            print("超时！检查任务状态...")
            # 超时后任务会被自动取消
            print(f"  task.done() = {task.done()}")
            print(f"  task.cancelled() = {task.cancelled()}")

    await with_timeout_check()


# =============================================================================
# Task.result() - 获取任务结果
# =============================================================================


async def demo_task_result() -> None:
    """示例 06：task.result() - 获取任务结果。"""
    print("\n\n== task.result() - 获取任务结果 ==\n")

    async def compute(value: int) -> int:
        await asyncio.sleep(0.2)
        return value * value

    # 创建并等待任务
    task = asyncio.create_task(compute(10))
    await task

    # 获取结果
    result = task.result()
    print(f"计算结果: 10 * 10 = {result}")


async def demo_task_result_before_done() -> None:
    """示例 07：在任务完成前调用 result() 的行为。"""
    print("\n== 任务未完成时调用 result() ==\n")

    async def slow_task() -> str:
        await asyncio.sleep(1)
        return "完成"

    task = asyncio.create_task(slow_task())

    # 任务还在运行，尝试获取结果
    print(f"任务运行中，task.done() = {task.done()}")

    try:
        # result() 会阻塞等待任务完成
        result = task.result()
        print(f"获取到结果: {result}")
    except asyncio.InvalidStateError:
        print("任务未完成，result() 抛出 InvalidStateError")
    except Exception as e:
        # Python 3.12+ 中，result() 会等待任务完成
        print(f"获取到结果: {e}")


# =============================================================================
# Task.exception() - 获取任务异常
# =============================================================================


async def demo_task_exception() -> None:
    """示例 08：task.exception() - 获取任务异常。"""
    print("\n== task.exception() - 获取任务异常 ==\n")

    async def failing_worker() -> str:
        await asyncio.sleep(0.2)
        raise ValueError("模拟错误")

    # 创建任务
    task = asyncio.create_task(failing_worker())

    # 等待任务完成
    try:
        await task
    except ValueError as e:
        print(f"捕获到异常: {e}")

    # 任务已完成且有异常
    print(f"\n任务状态:")
    print(f"  task.done() = {task.done()}")
    print(f"  task.exception() = {task.exception()}")

    # 如果任务有异常，调用 result() 会重新抛出
    try:
        task.result()
    except ValueError as e:
        print(f"  task.result() 重新抛出: {e}")


async def demo_exception_vs_result() -> None:
    """示例 09：exception() 与 result() 的对比。"""
    print("\n== exception() 与 result() 对比 ==\n")

    # 成功的任务
    async def success_task() -> str:
        await asyncio.sleep(0.1)
        return "成功"

    task1 = asyncio.create_task(success_task())
    await task1

    print(f"成功任务:")
    print(f"  task.result() = {task1.result()}")
    print(f"  task.exception() = {task1.exception()}")

    # 失败的任务
    async def fail_task() -> str:
        await asyncio.sleep(0.1)
        raise RuntimeError("失败")

    task2 = asyncio.create_task(fail_task())
    try:
        await task2
    except RuntimeError:
        pass

    print(f"\n失败任务:")
    print(f"  task.exception() = {task2.exception()}")
    print(f"  调用 task.result() 会重新抛出异常")


# =============================================================================
# 综合示例：任务状态管理
# =============================================================================


async def demo_task_status_monitor() -> None:
    """示例 10：综合 - 任务状态监控器。"""
    print("\n\n== 综合示例：任务状态监控器 ==\n")

    class TaskMonitor:
        """任务监控器：跟踪任务状态和结果。"""

        def __init__(self) -> None:
            self.tasks: dict[str, asyncio.Task[Any]] = {}

        async def run_task(self, name: str, coro) -> None:
            """运行并监控任务。"""
            task = asyncio.create_task(coro)
            self.tasks[name] = task
            print(f"[监控器] 任务 '{name}' 已创建")

        def status_report(self) -> None:
            """生成状态报告。"""
            print(f"\n[任务状态报告]")
            for name, task in self.tasks.items():
                if task.done():
                    if task.cancelled():
                        status = "已取消"
                    elif task.exception():
                        status = f"异常: {task.exception()}"
                    else:
                        status = f"完成: {task.result()}"
                else:
                    status = "运行中"
                print(f"  {name}: {status}")

    # 定义一些测试任务
    async def quick_task(name: str) -> str:
        await asyncio.sleep(0.2)
        return f"{name} 完成"

    async def slow_task(name: str) -> str:
        await asyncio.sleep(2.0)
        return f"{name} 完成"

    async def failing_task(name: str) -> str:
        await asyncio.sleep(0.3)
        raise ValueError(f"{name} 失败")

    # 创建监控器
    monitor = TaskMonitor()

    # 启动各种任务
    await monitor.run_task("快速任务", quick_task("快速任务"))
    await monitor.run_task("慢速任务", slow_task("慢速任务"))
    await monitor.run_task("失败任务", failing_task("失败任务"))

    # 定期检查状态
    for _ in range(5):
        await asyncio.sleep(0.2)
        monitor.status_report()

        # 如果慢速任务还在运行，取消它
        slow_task = monitor.tasks["慢速任务"]
        if not slow_task.done() and asyncio.get_event_loop().time() > 1.0:
            print(f"\n[监控器] 取消慢速任务...")
            slow_task.cancel()

    # 最终报告
    print(f"\n[最终状态]")
    monitor.status_report()


async def demo_task_group_with_status() -> None:
    """示例 11：TaskGroup 与状态检查结合。"""
    print("\n\n== TaskGroup + 状态检查 ==\n")

    results: dict[str, str | Exception] = {}

    async def worker(name: str, fail: bool = False) -> str:
        await asyncio.sleep(0.2)
        if fail:
            raise RuntimeError(f"{name} 失败")
        return f"{name} 成功"

    try:
        async with asyncio.TaskGroup() as tg:
            # 创建任务
            tg.create_task(worker("Task-1"))
            tg.create_task(worker("Task-2"))
            tg.create_task(worker("Task-3", fail=True))

    except ExceptionGroup as eg:
        print(f"捕获到异常组，包含 {len(eg.exceptions)} 个异常:")
        for exc in eg.exceptions:
            print(f"  - {exc}")

    print("\n注意：TaskGroup 会等待所有任务完成（成功或异常）")


# =============================================================================
# 最佳实践
# =============================================================================


async def demo_best_practices() -> None:
    """示例 12：任务状态管理最佳实践。"""
    print("\n\n== 任务状态管理最佳实践 ==\n")

    print("1. 使用 done() 检查任务是否完成:")
    print("   - 避免重复等待")
    print("   - 实现超时检查")

    print("\n2. 使用 cancelled() 检查取消状态:")
    print("   - 区分正常完成和被取消")
    print("   - 处理取消后的清理")

    print("\n3. 使用 result() 获取结果:")
    print("   - 只在 done() 为 True 后调用")
    print("   - 注意：result() 会重新抛出异常")

    print("\n4. 使用 exception() 获取异常:")
    print("   - 非破坏性：不会重新抛出")
    print("   - 返回 None 表示任务成功")

    print("\n5. 任务取消最佳实践:")
    print("   - 在协程中捕获 CancelledError")
    print("   - 执行清理后重新抛出")
    print("   - 使用 try/finally 确保清理")


async def main() -> None:
    """运行所有示例。"""
    # done() 示例
    await demo_task_done()
    await demo_task_done_multiple()

    # cancel/cancelled() 示例
    await demo_task_cancel()
    await demo_task_cancelled()
    await demo_cancel_with_timeout()

    # result() 示例
    await demo_task_result()
    await demo_task_result_before_done()

    # exception() 示例
    await demo_task_exception()
    await demo_exception_vs_result()

    # 综合示例
    await demo_task_status_monitor()
    await demo_task_group_with_status()

    # 最佳实践
    await demo_best_practices()

    print("\n" + "="*60)
    print("核心方法速查")
    print("="*60)
    print("\nasyncio.Task 状态方法:")
    print("  task.done()        → bool:   任务是否完成")
    print("  task.cancelled()   → bool:   任务是否被取消")
    print("  task.cancel()      → None:   取消任务")
    print("  task.result()      → Any:    获取结果（可能阻塞/抛异常）")
    print("  task.exception()   → Exception|None: 获取异常（不抛出）")
    print("\n使用建议:")
    print("  - 先检查 done()，再调用 result()/exception()")
    print("  - 使用 cancelled() 区分取消和正常完成")
    print("  - exception() 用于非破坏性检查异常")


if __name__ == "__main__":
    asyncio.run(main())
