#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：拼接与拆分。

运行：
    python3 02_Frameworks/02_Numpy/11_stack_split.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    print("a ->")
    print(a)
    print("b ->")
    print(b)

    print("
concatenate(axis=0) ->")
    print(np.concatenate([a, b], axis=0))

    print("
concatenate(axis=1) ->")
    print(np.concatenate([a, b], axis=1))

    print("
vstack ->")
    print(np.vstack([a, b]))

    print("
hstack ->")
    print(np.hstack([a, b]))

    print("
stack(axis=0) ->")
    print(np.stack([a, b], axis=0))

    print("
split ->")
    parts = np.split(np.arange(6), 3)
    print(parts)


if __name__ == "__main__":
    main()
