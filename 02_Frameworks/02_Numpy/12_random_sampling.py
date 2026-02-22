#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：随机数（可重复）。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/12_random_sampling.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(42)

    print("integers ->", rng.integers(0, 10, size=5))
    print("random((2,3)) ->")
    print(rng.random((2, 3)))

    print("\nchoice ->", rng.choice([10, 20, 30, 40], size=3, replace=False))

    arr = np.arange(5)
    rng.shuffle(arr)
    print("shuffle ->", arr)


if __name__ == "__main__":
    main()
