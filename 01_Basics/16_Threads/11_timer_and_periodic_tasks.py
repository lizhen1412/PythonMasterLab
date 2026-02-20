#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：Timer 与周期任务。
Author: Lambert
"""

from __future__ import annotations

import threading
import time


def demo_timer() -> None:
    def hello() -> None:
        print("[timer] hello after delay")

    timer = threading.Timer(0.2, hello)
    timer.start()
    timer.join()


def demo_periodic(stop_event: threading.Event, interval: float = 0.1) -> None:
    """用 while+sleep+Event 实现可停止的周期任务。"""
    while not stop_event.is_set():
        print("[periodic] tick")
        time.sleep(interval)


def main() -> None:
    print("== Timer 一次性 ==")
    demo_timer()

    print("\n== 周期任务（可停止） ==")
    stop_event = threading.Event()
    t = threading.Thread(target=demo_periodic, args=(stop_event,))
    t.start()
    time.sleep(0.35)
    stop_event.set()
    t.join()
    print("[main] stopped periodic task")
    print("提示：Timer 不精确，复杂调度请用专用调度器或系统定时任务。")


if __name__ == "__main__":
    main()