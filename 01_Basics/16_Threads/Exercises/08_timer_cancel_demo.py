#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：Timer 启动后在条件满足前取消。
Author: Lambert
"""

from __future__ import annotations

import threading
import time


def main() -> None:
    fired = threading.Event()

    def action() -> None:
        fired.set()
        print("[timer] fired")

    timer = threading.Timer(0.3, action)
    timer.start()
    time.sleep(0.1)
    cancelled = timer.cancel()
    print("timer cancelled?", cancelled)
    timer.join()  # 等待线程结束
    print("fired flag?", fired.is_set())


if __name__ == "__main__":
    main()