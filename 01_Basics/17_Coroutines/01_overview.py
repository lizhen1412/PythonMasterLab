#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 协程与 asyncio 章节索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/17_Coroutines/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_async_await_basics.py", "async/await 基础，asyncio.run、sleep、并发 vs 串行"),
    ("03_tasks_create_and_gather.py", "create_task、gather、as_completed，返回值与异常"),
    ("04_taskgroup_structured_concurrency.py", "TaskGroup（3.11+）结构化并发与异常传播"),
    ("05_timeout_and_cancel.py", "wait_for/asyncio.timeout、task.cancel、CancelledError"),
    ("06_asyncio_queue_and_sync_primitives.py", "asyncio.Queue 生产消费；Lock/Event/Semaphore 对比"),
    ("07_to_thread_and_blocking_calls.py", "asyncio.to_thread 包装阻塞函数，避免卡住事件循环"),
    ("08_tcp_echo_server_client.py", "本地 TCP echo server/client（不访问外网）"),
    ("09_async_context_and_iter.py", "async with 与 async for 示例"),
    ("10_error_handling_and_return_exceptions.py", "gather return_exceptions、后台任务异常处理"),
    ("11_fire_and_forget_caveats.py", "fire-and-forget 风险，添加回调监控异常"),
    ("12_asyncio_vs_threads_brief.py", "协程 vs 线程选择指南"),
    ("13_chapter_summary.py", "本章总结：规则清单与常见坑"),
    ("Exercises/01_overview.py", "练习题索引（每题一个文件）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()