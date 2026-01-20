#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：超时与取消。
"""

from __future__ import annotations

import concurrent.futures as cf
import threading
import time


def slow_task() -> str:
    time.sleep(0.5)
    return "done"


def join_with_timeout() -> None:
    t = threading.Thread(target=slow_task)
    t.start()
    finished = t.join(timeout=0.1)
    print("join timeout finished?", finished)
    t.join()
    print("thread finally joined")


def future_timeout_and_cancel() -> None:
    with cf.ThreadPoolExecutor(max_workers=1) as executor:
        fut = executor.submit(slow_task)
        try:
            fut.result(timeout=0.1)
        except cf.TimeoutError:
            print("future result timeout -> cancel?")
            cancelled = fut.cancel()
            print("cancelled?", cancelled)
        # 如果任务已开始运行，cancel 返回 False
        print("done?", fut.done(), "cancelled?", fut.cancelled())
        if not fut.cancelled():
            print("get actual result ->", fut.result())


def main() -> None:
    print("== join 超时 ==")
    join_with_timeout()

    print("\n== Future 超时/取消 ==")
    future_timeout_and_cancel()


if __name__ == "__main__":
    main()
