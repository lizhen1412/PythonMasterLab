#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：拼接与拆分。
Author: Lambert

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

    print("\nconcatenate(axis=0) ->")
    print(np.concatenate([a, b], axis=0))

    print("\nconcatenate(axis=1) ->")
    print(np.concatenate([a, b], axis=1))

    print("\nvstack ->")
    print(np.vstack([a, b]))

    print("\nhstack ->")
    print(np.hstack([a, b]))

    print("\nstack(axis=0) ->")
    print(np.stack([a, b], axis=0))

    print("\nsplit ->")
    parts = np.split(np.arange(6), 3)
    print(parts)


if __name__ == "__main__":
    main()
