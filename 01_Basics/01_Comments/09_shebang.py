#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：shebang（#!）示例。

说明：
- 在类 Unix 系统（macOS/Linux）中，如果脚本有可执行权限并以 `./script.py` 方式运行，
  操作系统会读取第一行 shebang 来选择解释器。
- 对 Python 解释器来说，shebang 这一行也只是“注释”。

你可以在终端中手动试试：
    chmod +x 01_Basics/01_Comments/09_shebang.py
    ./01_Basics/01_Comments/09_shebang.py
"""

from __future__ import annotations

import sys


def main() -> None:
    print("sys.executable =", sys.executable)
    print("argv[0]        =", sys.argv[0])
    print("python version =", sys.version.split()[0])


if __name__ == "__main__":
    main()
