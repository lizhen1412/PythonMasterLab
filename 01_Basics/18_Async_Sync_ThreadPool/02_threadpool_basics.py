#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：ThreadPoolExecutor 提交/结果/异常/超时/取消。
"""

from __future__ import annotations

import concurrent.futures as cf
import time
from typing import Any


def task(x: int) -> int:
    if x == 3:
        raise ValueError("boom")
    time.sleep(0.1)
    return x * 2


def main() -> None:
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        for fut in cf.as_completed(futures, timeout=2):
            try:
                print("result ->", fut.result())
            except Exception as exc:
                print("caught ->", type(exc).__name__, exc)

        # map 方式：异常会在迭代时抛出
        print("\n== executor.map ==")
        try:
            for value in executor.map(task, [1, 2, 3, 4], timeout=1):
                print("map value ->", value)
        except Exception as exc:
            print("map caught ->", type(exc).__name__, exc)

        # 取消未开始的任务示例
        pending = executor.submit(time.sleep, 0.5)
        cancelled = pending.cancel()
        print("cancel pending?", cancelled)


if __name__ == "__main__":
    main()
