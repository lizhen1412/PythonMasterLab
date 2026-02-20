#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：线程基础 - 创建/start/join、daemon、name/ident、join 超时。
Author: Lambert
"""

from __future__ import annotations

import threading
import time


def worker(duration: float, name: str) -> None:
    print(f"[{name}] start, ident={threading.get_ident()}, daemon={threading.current_thread().daemon}")
    time.sleep(duration)
    print(f"[{name}] done after {duration}s")


def demo_start_join() -> None:
    t = threading.Thread(target=worker, args=(0.5, "normal"))
    t.start()
    t.join()
    print("joined normal thread")


def demo_daemon() -> None:
    t = threading.Thread(target=worker, args=(1.0, "daemon"), daemon=True)
    t.start()
    t.join(timeout=0.2)
    print("daemon alive after timeout?", t.is_alive())
    # 程序退出时 daemon 线程会被强制结束，不能用于清理资源


def demo_join_timeout() -> None:
    t = threading.Thread(target=worker, args=(0.6, "timeout"))
    t.start()
    finished = t.join(timeout=0.1)
    print("join returned?", finished)
    t.join()
    print("finally joined")


def main() -> None:
    demo_start_join()
    print()
    demo_daemon()
    print()
    demo_join_timeout()


if __name__ == "__main__":
    main()