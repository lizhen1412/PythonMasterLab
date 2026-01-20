#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：密码/密钥输入（getpass，不回显）。

你会学到：
1) `getpass.getpass()`：从终端读取，不回显输入内容（更安全）
2) 不要打印真实密码；最多打印长度或掩码
3) getpass 需要“真实终端（TTY）”，在非交互环境会退化/告警，所以本例会做检测

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/09_getpass_secret_input.py
"""

from __future__ import annotations

import sys
from getpass import getpass


def main() -> None:
    # getpass 会把提示写到 stderr，并要求 stdin 是 TTY；否则可能出现 warning 或无法隐藏回显。
    if not (sys.stdin.isatty() and sys.stderr.isatty()):
        print("当前不是交互终端（TTY），跳过 getpass 演示。")
        print("请在真实终端中运行本脚本，然后按提示输入密码。")
        return

    secret = getpass("请输入密码（不会回显）：")
    print("len(secret) =", len(secret))
    print("masked      =", "*" * len(secret))


if __name__ == "__main__":
    main()

