#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：安装与版本检查（numpy 2.4.0）。
Author: Lambert

运行：
    python3 02_Frameworks/02_Numpy/02_install_and_version.py
"""

from __future__ import annotations

import numpy as np

EXPECTED = "2.4.0"


def main() -> None:
    print("numpy version ->", np.__version__)
    if np.__version__ != EXPECTED:
        print(f"警告：本章基于 numpy {EXPECTED}，当前为 {np.__version__}")

    arr = np.array([1, 2, 3])
    print("sample array ->", arr)


if __name__ == "__main__":
    main()