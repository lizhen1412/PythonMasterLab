#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：异步 + 同步 + 线程池协作章节索引。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/18_Async_Sync_ThreadPool/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_threadpool_basics.py", "ThreadPoolExecutor 提交/结果/异常/超时/取消"),
    ("03_cpu_vs_io_in_threadpool.py", "CPU 密集 vs I/O 模拟：线程池收益对比"),
    ("04_async_to_thread_basics.py", "async 中用 asyncio.to_thread 包装阻塞函数"),
    ("05_run_in_executor_legacy.py", "loop.run_in_executor（自建线程池）兼容旧代码"),
    ("06_limit_concurrency_with_semaphore.py", "Semaphore + to_thread 限制阻塞调用并发"),
    ("07_timeout_and_cancel_bridge.py", "wait_for/asyncio.timeout + to_thread，取消与清理"),
    ("08_async_producer_threadpool_consumer.py", "async 生产 + 线程池消费阻塞任务，哨兵退出"),
    ("09_threadpool_logging_and_cleanup.py", "线程名日志，shutdown(cancel_futures) 行为与清理"),
    ("10_what_not_to_do.py", "反例：线程池里 asyncio.run、无限制任务堆积"),
    ("11_chapter_summary.py", "本章总结：规则清单与常见坑"),
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