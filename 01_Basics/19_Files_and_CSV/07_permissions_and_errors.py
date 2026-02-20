#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：权限/错误处理：stat、chmod、异常捕获。
Author: Lambert
"""

from __future__ import annotations

import os
from pathlib import Path


def show_stat(path: Path) -> None:
    st = path.stat()
    print("size:", st.st_size, "mode:", oct(st.st_mode), "mtime:", st.st_mtime)


def chmod_example(path: Path) -> None:
    original_mode = path.stat().st_mode
    path.chmod(0o444)  # 只读
    try:
        try:
            path.write_text("should fail", encoding="utf-8")
        except PermissionError as exc:
            print("捕获 PermissionError ->", exc)
    finally:
        path.chmod(original_mode)


def missing_file_example(path: Path) -> None:
    try:
        path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        print("捕获 FileNotFoundError ->", exc)


def main() -> None:
    base = Path(__file__).resolve().parent
    sample = base / "perm.txt"
    sample.write_text("hello", encoding="utf-8")

    print("== stat ==")
    show_stat(sample)

    print("\n== chmod 示例 ==")
    chmod_example(sample)

    print("\n== 缺失文件示例 ==")
    missing_file_example(base / "not_exists.txt")

    sample.unlink(missing_ok=True)


if __name__ == "__main__":
    main()