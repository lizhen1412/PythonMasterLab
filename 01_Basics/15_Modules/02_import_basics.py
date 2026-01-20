#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：模块导入基础。

- `import module` / `import module as alias`
- `from module import name` / `from module import name as alias`
- `__name__`：脚本入口与模块导入的区别
- `sys.path`：解释器的模块搜索路径
"""

from __future__ import annotations

import math
import sys
from pathlib import Path


def demo_import_styles() -> None:
    """展示常见导入写法与效果。"""
    import random as rnd  # 局部导入也可以，但注意性能与循环导入

    print("math.sqrt(9) ->", math.sqrt(9))
    print("Path.cwd() ->", Path.cwd())
    print("rnd.randint(1, 3) ->", rnd.randint(1, 3))

    from collections import Counter as C

    counts = C("mississippi")
    print("Counter 导入重命名 ->", counts.most_common(2))


def show_sys_path(limit: int = 3) -> None:
    """打印模块搜索路径的前几项。"""
    print("sys.path 前几项：")
    for idx, entry in enumerate(sys.path[:limit], start=1):
        print(f"{idx:02d}. {entry}")


def main() -> None:
    print(f"当前模块 __name__ -> {__name__}")
    print("\n== 导入写法 ==")
    demo_import_styles()

    print("\n== 模块搜索路径 ==")
    show_sys_path()

    print("\n提示：当此文件被 import 时，main() 不会自动执行。")


if __name__ == "__main__":
    main()
