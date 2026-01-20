#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：Event 启停信号，优雅退出循环。
"""

from __future__ import annotations

import threading
import time


def worker(stop_event: threading.Event) -> None:
    print("[worker] waiting for stop event...")
    while not stop_event.is_set():
        print("[worker] working...")
        time.sleep(0.1)
    print("[worker] received stop signal, exiting.")


def main() -> None:
    stop_event = threading.Event()
    t = threading.Thread(target=worker, args=(stop_event,), name="event-worker")
    t.start()

    time.sleep(0.3)
    print("[main] set stop event")
    stop_event.set()
    t.join()
    print("[main] worker stopped")


if __name__ == "__main__":
    main()
