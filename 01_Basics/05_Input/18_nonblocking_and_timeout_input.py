#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 18：非阻塞/超时输入（select）。
Author: Lambert

你会学到：
1) select 等待 stdin 可读
2) 超时后返回 None（不阻塞）
3) Windows 上需要额外方案（这里只做提示）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/18_nonblocking_and_timeout_input.py
"""

from __future__ import annotations

import os
import select
import sys


def input_with_timeout(prompt: str, timeout: float) -> str | None:
    print(prompt, end="", flush=True)
    try:
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
    except (OSError, ValueError):
        return None
    if ready:
        return sys.stdin.readline().rstrip("\n")
    return None


def main() -> None:
    if os.name == "nt":
        print("Windows 提示：select 不支持 stdin；可用 msvcrt 或 asyncio 实现。")
        return
    if not sys.stdin.isatty():
        print("stdin 非 TTY：跳过交互超时演示。")
        return

    text = input_with_timeout("在 3 秒内输入一行：", timeout=3.0)
    if text is None:
        print("\n超时：未输入任何内容")
    else:
        print("\n读取到：", repr(text))


if __name__ == "__main__":
    main()