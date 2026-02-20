#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 03：打开模式/编码/newline/buffering，with/seek/tell。
Author: Lambert
"""

from __future__ import annotations

from pathlib import Path


def write_and_seek(tmp: Path) -> None:
    text = "hello\nworld\n"
    with tmp.open("w", encoding="utf-8", newline="") as f:
        f.write(text)
        pos = f.tell()
        print("写入后位置 ->", pos)

    with tmp.open("r", encoding="utf-8") as f:
        print("read() ->", f.read())
        f.seek(0)
        print("tell after seek ->", f.tell())
        line = f.readline()
        print("第一行 ->", line.strip())


def main() -> None:
    base = Path(__file__).resolve().parent
    tmp = base / "sample_text.txt"
    write_and_seek(tmp)
    tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()