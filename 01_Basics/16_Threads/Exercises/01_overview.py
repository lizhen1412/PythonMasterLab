#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：线程（Threads）章节练习（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/16_Threads/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_fix_race_with_lock.py", "修复计数竞态，使用 Lock"),
    ("03_use_semaphore_limit_concurrency.py", "Semaphore 限制并发任务数"),
    ("04_wait_with_event.py", "用 Event 控制工作线程开始/停止"),
    ("05_queue_worker_with_sentinel.py", "Queue 任务 + 哨兵退出，task_done/join"),
    ("06_executor_timeout_and_errors.py", "线程池多任务，处理异常与超时"),
    ("07_barrier_two_phase_task.py", "Barrier 同步两阶段工作"),
    ("08_timer_cancel_demo.py", "Timer 启动后在条件满足前取消"),
    ("09_log_thread_names.py", "logging 打印线程名，观察并发输出"),
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
