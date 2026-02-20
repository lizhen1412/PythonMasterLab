#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：协程与 asyncio（Coroutines）章节练习。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 01_Basics/17_Coroutines/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_run_two_coroutines.py", "并发运行两个 sleep，比较耗时"),
    ("03_use_gather_with_errors.py", "gather 处理异常（return_exceptions 对比）"),
    ("04_taskgroup_retry_on_failure.py", "TaskGroup 并发，失败任务打印日志"),
    ("05_queue_producer_consumer_async.py", "asyncio.Queue 生产消费，哨兵退出"),
    ("06_timeout_and_cancel_task.py", "wait_for 超时取消，捕获 CancelledError"),
    ("07_to_thread_blocking_io.py", "to_thread 包装阻塞函数，验证事件循环未被阻塞"),
    ("08_tcp_echo_roundtrip.py", "本地 async echo server + 客户端验证回显"),
    ("09_fire_and_forget_safe_wrapper.py", "封装 create_task，记录异常/结果"),
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