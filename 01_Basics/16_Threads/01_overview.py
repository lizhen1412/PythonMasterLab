#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 线程（Threads）章节索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/16_Threads/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_thread_basics_start_join.py", "创建/start/join、daemon、name/ident、join 超时"),
    ("03_race_condition_and_lock.py", "竞态反例 + Lock 修复"),
    ("04_reentrant_lock_and_semaphore.py", "RLock 重入示例；Semaphore 限制并发"),
    ("05_event_and_stop_flag.py", "Event 启停信号，优雅退出循环"),
    ("06_condition_and_barrier.py", "Condition 等待/通知；Barrier 阶段同步"),
    ("07_queue_producer_consumer.py", "Queue 生产者-消费者，哨兵退出"),
    ("08_threadpool_executor_basics.py", "ThreadPoolExecutor 提交/结果/异常/超时"),
    ("09_timeout_and_cancel.py", "join 超时；Future 取消/超时处理"),
    ("10_thread_exceptions_and_logging.py", "线程异常、excepthook、日志带线程名"),
    ("11_timer_and_periodic_tasks.py", "Timer 一次性；周期任务的替代方案"),
    ("12_gil_and_performance_notes.py", "GIL 说明：I/O vs CPU 密集对比"),
    ("13_asyncio_vs_threads_brief.py", "线程 vs asyncio 选择指南（简述）"),
    ("14_random_per_thread.py", "每线程独立 Random 避免共享状态干扰"),
    ("15_chapter_summary.py", "本章总结：规则清单与常见坑"),
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
