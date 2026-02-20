#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：查看/修改 sys.path。
Author: Lambert

要求：
- 打印前几项 sys.path，理解搜索顺序
- 临时插入一个路径，再还原
"""

from __future__ import annotations

import sys
from pathlib import Path


def show_sys_path(limit: int = 5) -> None:
    for idx, entry in enumerate(sys.path[:limit], start=1):
        print(f"{idx:02d}. {entry}")


def main() -> None:
    print("== 原始 sys.path ==")
    show_sys_path()

    temp = str(Path(__file__).parent)
    sys.path.insert(0, temp)
    print("\n== 插入练习路径后 ==")
    show_sys_path()

    # 还原
    sys.path.remove(temp)
    print("\n== 还原后 ==")
    show_sys_path()


if __name__ == "__main__":
    main()