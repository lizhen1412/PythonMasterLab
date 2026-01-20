#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：字符串处理（str 访问器）。

运行：
    python3 02_Frameworks/01_Pandas/12_string_methods.py
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series([" Alice ", "Bob", None, "cathy"])

    print("lower/strip ->")
    print(s.str.strip().str.lower())

    print("\ncontains 'a' ->")
    print(s.str.contains("a", case=False, na=False))

    print("\nreplace ->")
    print(s.str.replace("a", "@", case=False, regex=False))

    print("\nsplit ->")
    names = pd.Series(["alice:90", "bob:75"])
    print(names.str.split(":", expand=True))


if __name__ == "__main__":
    main()
