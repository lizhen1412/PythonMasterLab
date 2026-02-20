#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：演示 shutdown(cancel_futures=True) 对未开始任务的影响。
Author: Lambert
"""

from __future__ import annotations

import concurrent.futures as cf
import time


def slow(x: int) -> str:
    time.sleep(0.3)
    return f"slow-{x}"


def main() -> None:
    executor = cf.ThreadPoolExecutor(max_workers=1)
    futures = [executor.submit(slow, i) for i in range(3)]
    # 立即关闭并取消未开始任务
    executor.shutdown(wait=False, cancel_futures=True)
    for fut in futures:
        if fut.cancelled():
            print("future cancelled")
        else:
            try:
                print("result ->", fut.result(timeout=1))
            except Exception as exc:
                print("caught ->", type(exc).__name__, exc)


if __name__ == "__main__":
    main()