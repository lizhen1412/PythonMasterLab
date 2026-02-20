#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：安装与版本检查（pandas 2.3.3）。
Author: Lambert

运行（在仓库根目录执行）：
    python3 02_Frameworks/01_Pandas/02_install_and_version.py
"""

from __future__ import annotations

import pandas as pd

EXPECTED = "2.3.3"


def main() -> None:
    print("pandas version ->", pd.__version__)
    if pd.__version__ != EXPECTED:
        print(f"警告：本章基于 pandas {EXPECTED}，当前为 {pd.__version__}")

    s = pd.Series([1, 2, 3], name="demo")
    print("sample series ->")
    print(s)


if __name__ == "__main__":
    main()