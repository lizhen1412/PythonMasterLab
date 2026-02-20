#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：每线程独立 Random，避免共享状态干扰。
Author: Lambert
"""

from __future__ import annotations

import random
import threading
from typing import Dict


def worker(idx: int, results: Dict[int, list[int]]) -> None:
    rng = random.Random(idx)  # 每线程独立实例与种子
    nums = [rng.randint(1, 100) for _ in range(5)]
    results[idx] = nums
    print(f"[thread {idx}] {nums}")


def main() -> None:
    results: Dict[int, list[int]] = {}
    threads = [threading.Thread(target=worker, args=(i, results)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("汇总 ->", results)
    print("提示：random 在 CPython 有全局锁，但共享状态仍会交织，独立实例可避免干扰。")


if __name__ == "__main__":
    main()