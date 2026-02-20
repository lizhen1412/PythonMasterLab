#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：窗口函数（rolling/expanding/ewm）。
Author: Lambert

运行：
    python3 02_Frameworks/01_Pandas/18_window_rolling_ewm.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series([1, 2, 3, 4, 5])

    print("rolling(window=3).mean ->")
    print(s.rolling(window=3).mean())

    print("\nexpanding().sum ->")
    print(s.expanding().sum())

    print("\newm(span=3).mean ->")
    print(s.ewm(span=3, adjust=False).mean())


if __name__ == "__main__":
    main()