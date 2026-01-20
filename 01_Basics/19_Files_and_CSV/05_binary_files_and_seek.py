#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：二进制读写、偏移读取、seek。
"""

from __future__ import annotations

from pathlib import Path


def write_binary(path: Path) -> None:
    data = bytes(range(256))
    path.write_bytes(data)


def read_offsets(path: Path) -> None:
    with path.open("rb") as f:
        f.seek(100)
        chunk = f.read(10)
        print("从偏移 100 读 10 字节 ->", list(chunk))
        f.seek(-5, 2)  # 相对文件末尾
        tail = f.read()
        print("末尾 5 字节 ->", list(tail))


def main() -> None:
    base = Path(__file__).resolve().parent
    bin_path = base / "bytes.bin"
    write_binary(bin_path)
    read_offsets(bin_path)
    bin_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
