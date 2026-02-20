#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：Path 基础、遍历、stat 元数据。
Author: Lambert
"""

from __future__ import annotations

from pathlib import Path


def show_path_operations(base: Path) -> None:
    print("当前目录:", base)
    print("exists?", base.exists())
    print("is_dir?", base.is_dir())
    print("resolve ->", base.resolve())

    readme = base / "README.md"
    print("README exists?", readme.exists())
    if readme.exists():
        stat = readme.stat()
        print("size:", stat.st_size, "mtime:", stat.st_mtime)


def list_files(base: Path) -> None:
    print("\n== iterdir (前几项) ==")
    for path in list(base.iterdir())[:5]:
        print("-", path.name, "(dir)" if path.is_dir() else "(file)")

    print("\n== glob('**/*.py') 示例 (前 5 个) ==")
    for path in list(base.glob("**/*.py"))[:5]:
        print("-", path)


def main() -> None:
    base = Path(__file__).resolve().parent
    show_path_operations(base)
    list_files(base)


if __name__ == "__main__":
    main()