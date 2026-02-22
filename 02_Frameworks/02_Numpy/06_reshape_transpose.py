#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：reshape 与转置。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/06_reshape_transpose.py
"""

from __future__ import annotations

import numpy as np


def main() -> None:
    arr = np.arange(1, 13)
    print("arr ->", arr)

    mat = arr.reshape(3, 4)
    print("\nreshape(3,4) ->")
    print(mat)

    print("\nravel ->", mat.ravel())
    print("transpose ->")
    print(mat.T)

    print("\nswapaxes(0,1) ->")
    print(mat.swapaxes(0, 1))


if __name__ == "__main__":
    main()
