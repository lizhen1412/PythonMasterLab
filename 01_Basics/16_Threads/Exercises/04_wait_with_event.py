#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 04：用 Event 控制工作线程开始/停止。
"""

from __future__ import annotations

import threading
import time


def worker(start_event: threading.Event, stop_event: threading.Event) -> None:
    print("[worker] waiting for start")
    start_event.wait()
    print("[worker] started")
    while not stop_event.is_set():
        print("[worker] working...")
        time.sleep(0.05)
    print("[worker] stopping")


def main() -> None:
    start_event = threading.Event()
    stop_event = threading.Event()
    t = threading.Thread(target=worker, args=(start_event, stop_event))
    t.start()

    time.sleep(0.1)
    print("[main] set start")
    start_event.set()
    time.sleep(0.15)
    print("[main] set stop")
    stop_event.set()
    t.join()
    print("[main] done")


if __name__ == "__main__":
    main()
