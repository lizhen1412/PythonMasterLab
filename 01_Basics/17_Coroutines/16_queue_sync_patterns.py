#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：asyncio.Queue 同步模式 - task_done() 和 join()。
Author: Lambert

本示例演示 asyncio.Queue 的同步方法：

1. **task_done()** - 标记任务完成
2. **join()** - 等待所有任务完成

这些方法用于实现"生产者-消费者"模式的同步，确保：
- 所有队列中的项目都被处理完成
- 生产者知道消费者已经处理完所有数据
- 优雅关闭生产者-消费者系统

核心概念：
- 每次调用 get() 获取一个项目，处理后必须调用 task_done()
- join() 会阻塞，直到所有已获取的项目都标记为 task_done()
- 这是一种"倒计数"同步机制
"""

from __future__ import annotations

import asyncio
from typing import NoReturn


# =============================================================================
# 基础示例：task_done() 和 join()
# =============================================================================


async def demo_queue_join_basic() -> None:
    """示例 01：Queue 基础同步 - task_done() 和 join()。"""
    print("== Queue 基础同步：task_done() 和 join() ==\n")

    queue: asyncio.Queue[str] = asyncio.Queue()

    # 生产者：放入项目
    async def producer() -> None:
        for item in ["A", "B", "C"]:
            await queue.put(item)
            print(f"[生产者] 放入: {item}")
        print(f"[生产者] 完成放入，等待消费者处理...")

    # 消费者：取出并处理项目
    async def consumer() -> None:
        while True:
            # 获取项目（阻塞等待）
            item = await queue.get()
            print(f"[消费者] 取出: {item}")

            # 模拟处理
            await asyncio.sleep(0.1)

            # 标记任务完成（重要！）
            queue.task_done()
            print(f"[消费者] 完成处理: {item}")

    # 启动生产者和消费者
    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())

    # 等待生产者完成
    await producer_task
    print(f"\n[主控] 生产者完成，等待队列清空...")

    # 等待所有项目被处理（join() 会阻塞直到 task_done() 被调用相应次数）
    await queue.join()
    print(f"[主控] 队列已清空，所有项目处理完成")

    # 取消消费者任务（因为它是无限循环）
    consumer_task.cancel()
    try:
        await consumer_task
    except asyncio.CancelledError:
        pass


# =============================================================================
# 工作队列模式
# =============================================================================


async def demo_work_queue() -> None:
    """示例 02：工作队列 - 多个消费者处理任务。"""
    print("\n\n== 工作队列：多个消费者处理任务 ==\n")

    work_queue: asyncio.Queue[tuple[str, int]] = asyncio.Queue()

    async def worker(name: str) -> None:
        """工作协程：从队列获取并处理任务。"""
        while True:
            # 获取任务
            task_name, duration = await work_queue.get()
            print(f"[{name}] 开始: {task_name} (预计 {duration} 秒)")

            # 处理任务
            await asyncio.sleep(duration)

            # 标记完成
            work_queue.task_done()
            print(f"[{name}] 完成: {task_name}")

    # 生产者：创建多个任务
    tasks = [
        ("任务-1", 0.2),
        ("任务-2", 0.1),
        ("任务-3", 0.3),
        ("任务-4", 0.1),
        ("任务-5", 0.2),
    ]

    for task in tasks:
        await work_queue.put(task)

    # 启动多个工作协程
    workers = [
        asyncio.create_task(worker(f"Worker-{i}"))
        for i in range(3)
    ]

    # 等待所有任务完成
    print(f"[主控] 已放入 {len(tasks)} 个任务，等待处理...\n")
    await work_queue.join()
    print(f"\n[主控] 所有任务处理完成")

    # 取消工作协程
    for w in workers:
        w.cancel()

    # 等待取消完成
    await asyncio.gather(*workers, return_exceptions=True)


# =============================================================================
# 带计数模式
# =============================================================================


async def demo_pending_counter() -> None:
    """示例 03：追踪待处理任务数量。"""
    print("\n\n== 追踪待处理任务数量 ==\n")

    queue: asyncio.Queue[int] = asyncio.Queue()

    async def producer() -> None:
        """生产者：生成数字。"""
        for i in range(1, 6):
            await queue.put(i)
            print(f"[生产者] 放入: {i} | 待处理: {queue.qsize()}")
            await asyncio.sleep(0.1)

    async def consumer(name: str) -> None:
        """消费者：处理数字。"""
        while True:
            item = await queue.get()
            print(f"[{name}] 处理: {item} | 剩余: {queue.qsize() - 1}")

            await asyncio.sleep(0.15)  # 处理时间

            queue.task_done()

    # 启动生产者和消费者
    producer_task = asyncio.create_task(producer())
    consumers = [
        asyncio.create_task(consumer(f"Consumer-{i}"))
        for i in range(2)
    ]

    # 等待所有任务完成
    await queue.join()
    print(f"\n[主控] 所有任务完成")

    # 清理
    producer_task.cancel()
    for c in consumers:
        c.cancel()

    await asyncio.gather(producer_task, *consumers, return_exceptions=True)


# =============================================================================
# 批量处理模式
# =============================================================================


async def demo_batch_processing() -> None:
    """示例 04：批量处理 - 累积到一定数量后处理。"""
    print("\n\n== 批量处理模式 ==\n")

    class BatchProcessor:
        """批量处理器：累积项目到批次大小后处理。"""

        def __init__(self, batch_size: int) -> None:
            self.queue: asyncio.Queue[list[str]] = asyncio.Queue()
            self.batch_size = batch_size
            self.current_batch: list[str] = []

        async def add(self, item: str) -> None:
            """添加项目，达到批次大小时自动处理。"""
            self.current_batch.append(item)

            if len(self.current_batch) >= self.batch_size:
                # 满批次，放入队列处理
                batch = self.current_batch[:]
                self.current_batch.clear()
                await self.queue.put(batch)
                print(f"[添加] 满批次，放入队列: {batch}")

        async def finish(self) -> None:
            """完成添加，处理剩余项目。"""
            if self.current_batch:
                await self.queue.put(self.current_batch)
                print(f"[完成] 剩余批次放入队列: {self.current_batch}")
                self.current_batch.clear()

        async def processor(self, name: str) -> NoReturn:
            """批量处理器：从队列获取批次并处理。"""
            while True:
                batch = await self.queue.get()
                print(f"[{name}] 处理批次: {batch}")
                await asyncio.sleep(0.2)  # 模拟处理
                print(f"[{name}] 批次处理完成")
                self.queue.task_done()

    processor = BatchProcessor(batch_size=3)

    # 启动处理器
    processor_task = asyncio.create_task(processor.processor("Processor"))

    # 添加项目
    items = ["A", "B", "C", "D", "E", "F", "G"]
    for item in items:
        await processor.add(item)
        await asyncio.sleep(0.05)

    # 完成并等待
    await processor.finish()
    await processor.queue.join()
    print(f"\n[主控] 所有批次处理完成")

    processor_task.cancel()
    try:
        await processor_task
    except asyncio.CancelledError:
        pass


# =============================================================================
# 优雅关闭模式
# =============================================================================


async def demo_graceful_shutdown() -> None:
    """示例 05：优雅关闭 - 确保所有任务处理完成。"""
    print("\n\n== 优雅关闭模式 ==\n")

    class TaskSystem:
        """任务系统：支持优雅关闭。"""

        def __init__(self, num_workers: int) -> None:
            self.queue: asyncio.Queue[str] = asyncio.Queue()
            self.workers: list[asyncio.Task[None]] = []
            self.num_workers = num_workers
            self.shutting_down = False

        async def worker(self, name: str) -> NoReturn:
            """工作协程。"""
            while not self.shutting_down or not self.queue.empty():
                try:
                    # 使用 get_nowait() 避免在关闭时阻塞
                    task = await asyncio.wait_for(self.queue.get(), timeout=0.5)
                    print(f"[{name}] 处理: {task}")
                    await asyncio.sleep(0.2)  # 模拟处理
                    self.queue.task_done()
                    print(f"[{name}] 完成: {task}")
                except asyncio.TimeoutError:
                    continue

        async def start(self) -> None:
            """启动工作协程。"""
            self.workers = [
                asyncio.create_task(self.worker(f"Worker-{i}"))
                for i in range(self.num_workers)
            ]
            print(f"[系统] 启动 {self.num_workers} 个工作协程")

        async def submit(self, task: str) -> None:
            """提交任务。"""
            if self.shutting_down:
                print(f"[系统] 拒绝任务（系统关闭中）: {task}")
                return
            await self.queue.put(task)
            print(f"[系统] 提交任务: {task}")

        async def shutdown(self) -> None:
            """优雅关闭：等待所有任务完成。"""
            self.shutting_down = True
            print(f"[系统] 开始优雅关闭...")

            # 等待队列中的任务完成
            await self.queue.join()
            print(f"[系统] 队列任务已清空")

            # 取消工作协程
            for w in self.workers:
                w.cancel()

            # 等待取消完成
            await asyncio.gather(*self.workers, return_exceptions=True)
            print(f"[系统] 工作协程已关闭")

    # 创建任务系统
    system = TaskSystem(num_workers=3)
    await system.start()

    # 提交任务
    tasks = [f"Task-{i}" for i in range(1, 8)]
    for task in tasks:
        await system.submit(task)
        await asyncio.sleep(0.1)

    # 优雅关闭
    await system.shutdown()


# =============================================================================
# 错误处理模式
# =============================================================================


async def demo_error_handling() -> None:
    """示例 06：错误处理 - 即使任务失败也要调用 task_done()。"""
    print("\n\n== 错误处理模式 ==\n")

    class SafeQueue(asyncio.Queue):
        """安全的队列：自动处理 task_done()。"""

        async def safe_get(self) -> Any:
            """获取并自动标记完成。"""
            item = await self.get()
            return item

        async def process_with_retry(self, max_retries: int = 3) -> None:
            """获取并处理，带重试机制。"""
            item = await self.get()

            for attempt in range(max_retries):
                try:
                    # 模拟可能失败的处理
                    if item == "fail":
                        raise RuntimeError("处理失败")

                    print(f"处理成功: {item}")
                    self.task_done()
                    return

                except Exception as e:
                    print(f"尝试 {attempt + 1}/{max_retries} 失败: {e}")
                    if attempt == max_retries - 1:
                        # 最后一次尝试也失败，但仍标记完成
                        print(f"放弃处理: {item}")
                        self.task_done()
                        return
                    await asyncio.sleep(0.1)

    queue: SafeQueue[str] = SafeQueue()

    # 放入测试项目
    items = ["A", "fail", "B", "fail", "C"]
    for item in items:
        await queue.put(item)

    # 处理所有项目（使用计数器避免竞态条件）
    async def processor(item_count: int) -> None:
        for _ in range(item_count):
            await queue.process_with_retry()

    await processor(len(items))
    await queue.join()
    print(f"\n[主控] 所有项目处理完成（包括失败的）")


# =============================================================================
# 性能监控模式
# =============================================================================


async def demo_performance_monitoring() -> None:
    """示例 07：性能监控 - 追踪吞吐量和延迟。"""
    print("\n\n== 性能监控模式 ==\n")

    class MonitoredQueue:
        """带监控的队列系统。"""

        def __init__(self) -> None:
            self.queue: asyncio.Queue[str] = asyncio.Queue()
            self.total_processed = 0
            self.start_time = 0

        async def worker(self, name: str) -> NoReturn:
            """工作协程：记录处理时间。"""
            while True:
                task = await self.queue.get()
                task_start = asyncio.get_event_loop().time()

                # 处理任务
                await asyncio.sleep(0.1)

                task_time = asyncio.get_event_loop().time() - task_start
                self.total_processed += 1
                print(f"[{name}] 处理: {task} | 耗时: {task_time:.3f}s | 总计: {self.total_processed}")

                self.queue.task_done()

        async def submit_batch(self, tasks: list[str]) -> None:
            """批量提交任务。"""
            self.start_time = asyncio.get_event_loop().time()
            for task in tasks:
                await self.queue.put(task)

        async def wait_completion(self) -> None:
            """等待完成并打印统计。"""
            await self.queue.join()
            elapsed = asyncio.get_event_loop().time() - self.start_time
            throughput = self.total_processed / elapsed if elapsed > 0 else 0

            print(f"\n[性能统计]")
            print(f"  总任务数: {self.total_processed}")
            print(f"  总耗时: {elapsed:.3f}s")
            print(f"  吞吐量: {throughput:.2f} 任务/秒")

    mq = MonitoredQueue()

    # 启动工作协程
    workers = [
        asyncio.create_task(mq.worker(f"Worker-{i}"))
        for i in range(3)
    ]

    # 提交任务
    tasks = [f"Task-{i}" for i in range(1, 16)]
    await mq.submit_batch(tasks)

    # 等待完成
    await mq.wait_completion()

    # 清理
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)


# =============================================================================
# 主函数
# =============================================================================


async def main() -> None:
    """运行所有示例。"""
    await demo_queue_join_basic()
    await demo_work_queue()
    await demo_pending_counter()
    await demo_batch_processing()
    await demo_graceful_shutdown()
    await demo_error_handling()
    await demo_performance_monitoring()

    print("\n" + "="*60)
    print("核心方法速查")
    print("="*60)
    print("\nasyncio.Queue 同步方法:")
    print("  await queue.get()       → 获取项目（阻塞）")
    print("  await queue.join()      → 等待所有项目标记为完成")
    print("  queue.task_done()       → 标记一个项目完成（重要！）")
    print("\n工作流程:")
    print("  1. 生产者: queue.put(item)")
    print("  2. 消费者: item = await queue.get()")
    print("  3. 消费者处理 item...")
    print("  4. 消费者: queue.task_done()  # 必须！")
    print("  5. 生产者: await queue.join()  # 等待所有 task_done()")
    print("\n常见错误:")
    print("  - 忘记调用 task_done(): join() 永远阻塞")
    print("  - 多次调用 task_done(): join() 提前完成")
    print("  - 不处理异常就退出: task_done() 永远不会调用")


if __name__ == "__main__":
    asyncio.run(main())
