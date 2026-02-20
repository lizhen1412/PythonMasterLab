#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：包结构、`__init__.py`、相对导入与 `__all__`。
Author: Lambert

要点速览：
- “包”本质上是带有 `__init__.py` 的目录；目录名就是包名
- 相对导入（例如 `from . import submodule`）只能在“包内部”使用
- `__all__` 可控制 `from package import *` 时导出哪些符号
- `__package__` / `__file__` 帮助我们了解模块所在位置

本示例不创建额外包，而是通过标准库模块观察元数据。
"""

from __future__ import annotations

import json
import random
from importlib import import_module


def describe_module(name: str) -> None:
    """打印模块的元数据。"""
    mod = import_module(name)
    print(f"[{name}] __name__={mod.__name__}, __package__={getattr(mod, '__package__', None)}, __file__={getattr(mod, '__file__', None)}")


def show_all_exports() -> None:
    """查看 __all__ 的作用（随机模块有定义）。"""
    print("random.__all__ 前 8 个 ->", random.__all__[:8])
    # 如果执行 from random import *，只会导入 __all__ 列出的名称


def explain_relative_imports() -> None:
    """文本说明相对导入的规则。"""
    print(
        "相对导入示例：在包内的 foo/bar.py 里写 `from . import baz`，"
        "只能在包内部使用；作为脚本直接运行可能触发 ImportError。"
    )
    print("顶层脚本若要导入同级模块，请使用绝对导入并确保工作目录/环境变量正确。")


def main() -> None:
    print("== 模块与包元数据 ==")
    describe_module("json")
    describe_module("pathlib")

    print("\n== __all__ 示例 ==")
    show_all_exports()

    print("\n== 相对导入说明 ==")
    explain_relative_imports()


if __name__ == "__main__":
    main()