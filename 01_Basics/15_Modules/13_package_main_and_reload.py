#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：包入口与模块重载。

- `python -m package.module`：以模块路径运行（常用于包内脚本）
- `__main__.py`：让 `python -m package` 直接运行包
- 模块缓存：`import` 只执行一次；`importlib.reload` 可强制重新执行
"""

from __future__ import annotations

import importlib
import sys


def explain_module_mode() -> None:
    """展示如何用 -m 运行模块/包。"""
    print("运行本文件的两种方式：")
    print("1) 直接脚本：python3 01_Basics/15_Modules/13_package_main_and_reload.py")
    print("2) 模块方式（示例）：python3 -m mypkg.tools.cli  # 需要合法包名")
    print("包入口示例：在包目录内放 __main__.py，可用 `python -m 包名` 运行（如 `python -m http.server`）")


def reload_demo() -> None:
    """用 importlib.reload 重新执行模块代码（演示效果）。"""
    import random

    random.seed(1)
    print("初始 randint ->", random.randint(1, 100))

    random.seed(999)
    print("重设种子后 randint ->", random.randint(1, 100))

    # reload 会重新执行模块顶层代码，但不会重置已变更的全局状态 unless 模块本身这么做
    reloaded = importlib.reload(random)
    print("reload(random) 返回 ->", reloaded)
    print("reload 后 randint ->", random.randint(1, 100))
    print("提醒：reload 可能留下旧引用，慎用于生产；更安全是重新启动进程或用 importlib.resources 读取数据。")


def cache_demo() -> None:
    """观察模块缓存：相同模块多次 import 只执行一次。"""
    import math

    before = "math" in sys.modules
    _ = importlib.import_module("math")
    after = "math" in sys.modules
    print(f"math 在 sys.modules 里? 导入前 {before}, 导入后 {after}")
    print("再次导入 math 不会重复执行模块顶层代码（通常是常量定义）。")


def main() -> None:
    explain_module_mode()
    print("\n== 模块缓存与 reload ==")
    print("sys.modules 里缓存已导入的模块；reload 会重新执行模块顶层代码。")
    cache_demo()
    reload_demo()


if __name__ == "__main__":
    main()
