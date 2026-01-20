#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：异步 + 同步 + 线程池协作章节练习。

运行方式（在仓库根目录执行）：
    python3 01_Basics/18_Async_Sync_ThreadPool/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_submit_io_tasks.py", "线程池并发假 I/O，收集结果"),
    ("03_compare_cpu_io_threadpool.py", "对比线程池处理 CPU vs I/O 耗时"),
    ("04_async_to_thread_wrapper.py", "封装 to_thread，限流并记录异常"),
    ("05_run_in_executor_limit.py", "自建线程池 + run_in_executor 提交多任务，限制并发"),
    ("06_wait_for_timeout_cleanup.py", "wait_for 包装 to_thread，超时后清理"),
    ("07_async_producer_thread_consumer.py", "asyncio.Queue 生产、线程池消费（阻塞），哨兵退出"),
    ("08_shutdown_cancel_futures.py", "演示 shutdown(cancel_futures=True) 对未开始任务的影响"),
    ("09_logging_thread_names_async.py", "logging 打印线程名与 async 上下文，运行混合任务"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习题清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
