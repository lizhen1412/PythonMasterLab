#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：环境变量输入（os.environ / os.getenv）。

你会学到：
1) 读取环境变量并设置默认值
2) 常见类型转换：int / bool
3) 环境变量只影响当前进程

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/14_environment_variables.py
"""

from __future__ import annotations

import os


def parse_bool(text: str | None, default: bool = False) -> bool:
    if text is None:
        return default
    normalized = text.strip().lower()
    if normalized in {"1", "true", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "no", "n", "off"}:
        return False
    return default


def main() -> None:
    os.environ.setdefault("APP_PORT", "8000")
    os.environ.setdefault("DEBUG", "true")

    port = int(os.getenv("APP_PORT", "8080"))
    debug = parse_bool(os.getenv("DEBUG"), default=False)
    mode = os.environ.get("APP_MODE", "dev")

    print("APP_PORT ->", port)
    print("DEBUG    ->", debug)
    print("APP_MODE ->", mode)

    print("\nTIP: try running with APP_PORT=9000 DEBUG=0 APP_MODE=prod")


if __name__ == "__main__":
    main()
