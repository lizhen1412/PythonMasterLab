#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：二进制按块读取并统计长度。
Author: Lambert
"""

from __future__ import annotations

from pathlib import Path


def read_chunks(path: Path, size: int = 4) -> list[bytes]:
    chunks: list[bytes] = []
    with path.open("rb") as f:
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            chunks.append(chunk)
    return chunks


def main() -> None:
    base = Path(__file__).resolve().parent
    bin_path = base / "bytes.bin"
    bin_path.write_bytes(bytes(range(16)))
    chunks = read_chunks(bin_path, size=5)
    print("块数 ->", len(chunks), "总长度 ->", sum(len(c) for c in chunks))
    bin_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()