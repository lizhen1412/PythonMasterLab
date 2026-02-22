#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：asyncio.Event 和 asyncio.Condition。
Author: Lambert

本示例演示 asyncio 的两个重要同步原语：

1. **asyncio.Event** - 事件标志
   - 用于协程间简单通知：一个协程发出信号，其他协程等待
   - 类似 threading.Event，但异步版本
   - 核心方法：set()、clear()、is_set()、wait()

2. **asyncio.Condition** - 条件变量
   - 用于复杂的等待/通知模式
   - 可以等待特定条件成立
   - 核心方法：acquire()、release()、wait()、notify()、notify_all()、wait_for()
"""

from __future__ import annotations

import asyncio


# =============================================================================
# asyncio.Event 示例
# =============================================================================


async def demo_event_basic() -> None:
    """示例 01：Event 基础用法。"""
    print("== Event 基础用法 ==\n")

    event = asyncio.Event()
    print(f"1. 初始状态: event.is_set() = {event.is_set()}")

    # 创建等待任务的协程
    async def waiter(name: str, delay: float) -> None:
        print(f"   [{name}] 等待事件...")
        await event.wait()
        print(f"   [{name}] 事件已触发！继续执行")

    # 启动多个等待任务
    tasks = [
        asyncio.create_task(waiter(f"Task-{i}", i * 0.1))
        for i in range(3)
    ]

    # 等待一下，让任务都开始等待
    await asyncio.sleep(0.2)

    # 触发事件
    print(f"\n2. 触发事件: event.set()")
    event.set()
    print(f"   状态: event.is_set() = {event.is_set()}")

    # 等待所有任务完成
    await asyncio.gather(*tasks)

    # 清除事件
    print(f"\n3. 清除事件: event.clear()")
    event.clear()
    print(f"   状态: event.is_set() = {event.is_set()}")


async def demo_event_publisher_subscriber() -> None:
    """示例 02：发布-订阅模式（Event 用于启动/停止信号）。"""
    print("\n== Event：发布-订阅模式（启动/停止信号）==\n")

    # 使用 Event 作为控制信号
    start_event = asyncio.Event()
    stop_event = asyncio.Event()

    async def worker(worker_id: int) -> None:
        """工作协程：等待启动信号，工作直到停止信号。"""
        # 等待启动信号
        print(f"[Worker-{worker_id}] 等待启动...")
        await start_event.wait()
        print(f"[Worker-{worker_id}] 已启动，开始工作")

        # 工作循环
        count = 0
        while not stop_event.is_set():
            print(f"[Worker-{worker_id}] 工作中... {count}")
            await asyncio.sleep(0.2)
            count += 1
            # 最多工作 3 次
            if count >= 3:
                break

        print(f"[Worker-{worker_id}] 收到停止信号，退出")

    # 启动多个工作协程
    workers = [asyncio.create_task(worker(i)) for i in range(3)]

    # 模拟启动时间
    await asyncio.sleep(0.3)
    print(f"\n[主控] 触发启动信号")
    start_event.set()

    # 让工作协程运行一段时间
    await asyncio.sleep(0.8)

    print(f"\n[主控] 触发停止信号")
    stop_event.set()

    # 等待所有工作协程完成
    await asyncio.gather(*workers)


async def demo_event_timeout() -> None:
    """示例 03：等待 Event 的超时处理。"""
    print("\n== Event：超时等待 ==\n")

    event = asyncio.Event()

    async def wait_with_timeout(name: str, timeout: float) -> None:
        """等待事件，带超时。"""
        try:
            print(f"[{name}] 等待事件（超时 {timeout} 秒）...")
            await asyncio.wait_for(event.wait(), timeout=timeout)
            print(f"[{name}] 事件已触发！")
        except asyncio.TimeoutError:
            print(f"[{name}] 等待超时")

    # 创建不同超时的等待任务
    tasks = [
        asyncio.create_task(wait_with_timeout("Task-1", 0.5)),
        asyncio.create_task(wait_with_timeout("Task-2", 1.5)),
    ]

    # 1 秒后触发事件
    await asyncio.sleep(1.0)
    print(f"\n[主控] 触发事件")
    event.set()

    await asyncio.gather(*tasks, return_exceptions=True)


async def demo_event_race_condition() -> None:
    """示例 04：使用 Event 避免竞态条件。"""
    print("\n== Event：避免竞态条件（初始化完成信号）==\n")

    class AsyncCache:
        """异步缓存：确保初始化完成后才能使用。"""

        def __init__(self) -> None:
            self._cache: dict[str, str] = {}
            self._initialized = asyncio.Event()

        async def initialize(self) -> None:
            """初始化缓存（模拟从数据库加载）。"""
            print(f"[缓存] 开始初始化...")
            await asyncio.sleep(0.5)  # 模拟加载时间
            self._cache = {"key1": "value1", "key2": "value2"}
            self._initialized.set()
            print(f"[缓存] 初始化完成")

        async def get(self, key: str) -> str | None:
            """获取缓存值（等待初始化完成）。"""
            await self._initialized.wait()  # 确保已初始化
            return self._cache.get(key)

    cache = AsyncCache()

    # 启动初始化和获取任务
    async def getter(name: str, key: str) -> None:
        print(f"[{name}] 尝试获取 {key}...")
        value = await cache.get(key)
        print(f"[{name}] 获取到: {key} = {value}")

    # 同时启动初始化和多个获取任务
    # 即使获取任务先执行，也会等待初始化完成
    tasks = [
        asyncio.create_task(cache.initialize()),
        asyncio.create_task(getter("Getter-1", "key1")),
        asyncio.create_task(getter("Getter-2", "key2")),
    ]

    await asyncio.gather(*tasks)


# =============================================================================
# asyncio.Condition 示例
# =============================================================================


async def demo_condition_basic() -> None:
    """示例 05：Condition 基础用法。"""
    print("\n\n== Condition 基础用法 ==\n")

    condition = asyncio.Condition()
    shared_resource: list[str] = []

    async def producer(name: str) -> None:
        """生产者：添加数据并通知。"""
        for i in range(2):
            async with condition:
                item = f"{name}-item-{i}"
                shared_resource.append(item)
                print(f"[{name}] 生产: {item}")
                # 通知一个等待的消费者
                condition.notify(1)
            await asyncio.sleep(0.1)

    async def consumer(name: str) -> None:
        """消费者：等待数据并消费。"""
        for _ in range(2):
            async with condition:
                # 等待条件成立（有数据可消费）
                while len(shared_resource) == 0:
                    print(f"[{name}] 等待数据...")
                    await condition.wait()

                item = shared_resource.pop(0)
                print(f"[{name}] 消费: {item}")

    # 启动生产者和消费者
    producers = [asyncio.create_task(producer(f"Producer-{i}")) for i in range(2)]
    consumers = [asyncio.create_task(consumer(f"Consumer-{i}")) for i in range(2)]

    await asyncio.gather(*producers, *consumers)
    print(f"\n最终状态: shared_resource = {shared_resource}")


async def demo_condition_wait_for() -> None:
    """示例 06：Condition.wait_for() - 等待条件谓词。"""
    print("\n== Condition：wait_for 等待条件谓词 ==\n")

    condition = asyncio.Condition()
    buffer_size = 0

    async def producer() -> None:
        """生产者：增加到缓冲区。"""
        nonlocal buffer_size
        for i in range(5):
            async with condition:
                buffer_size += 1
                print(f"[生产者] 添加数据，缓冲区大小: {buffer_size}")
                condition.notify(2)  # 通知两个消费者
            await asyncio.sleep(0.1)

    async def consumer(name: str, min_size: int) -> None:
        """消费者：等待缓冲区达到最小大小。"""
        nonlocal buffer_size

        async with condition:
            # wait_for 会一直等待，直到谓词返回 True
            print(f"[{name}] 等待缓冲区 >= {min_size}...")
            await condition.wait_for(lambda: buffer_size >= min_size)

            # 消费数据
            buffer_size -= 1
            print(f"[{name}] 消费数据，缓冲区大小: {buffer_size}")

    # 启动任务
    producer_task = asyncio.create_task(producer())

    # 创建不同需求的消费者
    consumers = [
        asyncio.create_task(consumer("Consumer-1", 1)),
        asyncio.create_task(consumer("Consumer-2", 2)),
        asyncio.create_task(consumer("Consumer-3", 3)),
    ]

    await producer_task
    await asyncio.gather(*consumers)


async def demo_condition_bounded_buffer() -> None:
    """示例 07：有界缓冲区（经典生产者-消费者问题）。"""
    print("\n== Condition：有界缓冲区 ==\n")

    class BoundedBuffer:
        """有界缓冲区：使用 Condition 实现生产者-消费者同步。"""

        def __init__(self, capacity: int) -> None:
            self.buffer: list[str] = []
            self.capacity = capacity
            self.condition = asyncio.Condition()

        async def put(self, item: str) -> None:
            """放入数据：如果满了就等待。"""
            async with self.condition:
                # 等待缓冲区有空间
                await self.condition.wait_for(lambda: len(self.buffer) < self.capacity)
                self.buffer.append(item)
                print(f"  [放入] {item} | 缓冲区: {len(self.buffer)}/{self.capacity}")
                # 通知消费者
                self.condition.notify(1)

        async def get(self) -> str:
            """取出数据：如果空了就等待。"""
            async with self.condition:
                # 等待缓冲区有数据
                await self.condition.wait_for(lambda: len(self.buffer) > 0)
                item = self.buffer.pop(0)
                print(f"  [取出] {item} | 缓冲区: {len(self.buffer)}/{self.capacity}")
                # 通知生产者
                self.condition.notify(1)
                return item

    buffer = BoundedBuffer(capacity=3)

    async def producer(name: str, items: list[str]) -> None:
        """生产者：生产多个物品。"""
        for item in items:
            await asyncio.sleep(0.15)  # 生产间隔
            await buffer.put(item)
        print(f"[{name}] 生产完成")

    async def consumer(name: str, count: int) -> None:
        """消费者：消费多个物品。"""
        for _ in range(count):
            await asyncio.sleep(0.1)  # 消费间隔
            item = await buffer.get()
        print(f"[{name}] 消费完成")

    # 启动生产者和消费者
    tasks = [
        asyncio.create_task(producer("Producer-1", ["A1", "A2", "A3"])),
        asyncio.create_task(producer("Producer-2", ["B1", "B2"])),
        asyncio.create_task(consumer("Consumer-1", 3)),
        asyncio.create_task(consumer("Consumer-2", 2)),
    ]

    await asyncio.gather(*tasks)


async def demo_condition_notify_all() -> None:
    """示例 08：notify_all() - 广播通知。"""
    print("\n== Condition：notify_all 广播通知 ==\n")

    condition = asyncio.Condition()
    ready = False

    async def worker(name: str) -> None:
        """工作协程：等待就绪信号。"""
        async with condition:
            print(f"[{name}] 等待就绪信号...")
            await condition.wait()
            print(f"[{name}] 收到信号，开始工作")
        # 模拟工作
        await asyncio.sleep(0.1)
        print(f"[{name}] 工作完成")

    async def starter() -> None:
        """启动协程：准备完成后广播通知。"""
        nonlocal ready
        await asyncio.sleep(0.3)

        async with condition:
            print(f"\n[启动器] 准备完成，广播启动信号...")
            ready = True
            condition.notify_all()  # 通知所有等待的协程

    # 启动多个工作协程
    workers = [asyncio.create_task(worker(f"Worker-{i}")) for i in range(5)]

    # 启动启动器
    starter_task = asyncio.create_task(starter())

    await asyncio.gather(*workers, starter_task)


# =============================================================================
# Event vs Condition 对比
# =============================================================================


async def demo_event_vs_condition() -> None:
    """示例 09：Event 与 Condition 的使用场景对比。"""
    print("\n\n== Event vs Condition 使用场景 ==\n")

    print("Event 适用场景：")
    print("  - 简单的一次性信号（启动/停止）")
    print("  - 广播通知（所有等待者都被唤醒）")
    print("  - 不关心条件，只等触发")

    print("\nCondition 适用场景：")
    print("  - 复杂的等待条件（缓冲区大小、资源状态）")
    print("  - 精细控制通知数量（notify(n)）")
    print("  - 需要检查特定条件谓词")


async def main() -> None:
    """运行所有示例。"""
    # Event 示例
    await demo_event_basic()
    await demo_event_publisher_subscriber()
    await demo_event_timeout()
    await demo_event_race_condition()

    # Condition 示例
    await demo_condition_basic()
    await demo_condition_wait_for()
    await demo_condition_bounded_buffer()
    await demo_condition_notify_all()

    # 对比
    await demo_event_vs_condition()

    print("\n" + "="*60)
    print("核心方法速查")
    print("="*60)
    print("\nasyncio.Event:")
    print("  - event.set()         触发事件")
    print("  - event.clear()       清除事件")
    print("  - event.is_set()      检查是否已触发")
    print("  - await event.wait()  等待事件触发")
    print("\nasyncio.Condition:")
    print("  - async with cond:    获取锁（上下文管理器）")
    print("  - await cond.wait()   等待通知（需持有锁）")
    print("  - cond.notify(n=1)    唤醒 n 个等待者")
    print("  - cond.notify_all()   唤醒所有等待者")
    print("  - await cond.wait_for(lambda: ...)  等待条件成立")


if __name__ == "__main__":
    asyncio.run(main())
