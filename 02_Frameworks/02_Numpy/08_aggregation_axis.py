#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：聚合与 axis。

运行：
    python3 02_Frameworks/02_Numpy/08_aggregation_axis.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.arange(1, 13).reshape(3, 4)
    print("arr ->")
    print(arr)

    print("
sum ->", arr.sum())
    print("sum(axis=0) ->", arr.sum(axis=0))
    print("sum(axis=1) ->", arr.sum(axis=1))

    print("
mean(axis=0, keepdims=True) ->")
    print(arr.mean(axis=0, keepdims=True))

    print("
max ->", arr.max())
    print("argmax ->", arr.argmax())


if __name__ == "__main__":
    main()
