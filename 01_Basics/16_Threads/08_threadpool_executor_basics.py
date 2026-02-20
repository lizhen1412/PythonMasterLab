#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：ThreadPoolExecutor 提交/结果/异常/超时。
Author: Lambert
"""

from __future__ import annotations

import concurrent.futures as cf
import time


def task(x: int) -> float:
    if x == 5:
        raise ValueError("boom")
    time.sleep(0.1)
    return x * 2


def main() -> None:
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(7)]
        for fut in cf.as_completed(futures, timeout=2):
            try:
                result = fut.result()
                print("result ->", result)
            except Exception as exc:
                print("caught exception ->", type(exc).__name__, exc)

        # map 会在取结果时抛出异常
        print("\n== executor.map（异常在迭代时抛出） ==")
        try:
            for value in executor.map(task, [1, 5, 2], timeout=2):
                print("map value ->", value)
        except Exception as exc:
            print("map caught ->", type(exc).__name__, exc)


if __name__ == "__main__":
    main()