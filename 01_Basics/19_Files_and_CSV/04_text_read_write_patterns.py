#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：文本读写模式：逐行/分块/错误处理。
"""

from __future__ import annotations

from pathlib import Path


def write_lines(path: Path) -> None:
    lines = ["苹果", "香蕉", "樱桃"]
    path.write_text("\n".join(lines), encoding="utf-8")


def read_line_by_line(path: Path) -> None:
    with path.open("r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            print(f"第 {idx} 行:", line.strip())


def read_in_chunks(path: Path, size: int = 8) -> None:
    with path.open("r", encoding="utf-8") as f:
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            print("块:", repr(chunk))


def handle_errors(path: Path) -> None:
    bad_bytes = b"\xff\xfe\xfd"
    path.write_bytes(bad_bytes)
    try:
        path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        print("捕获解码错误 ->", exc)
    # 忽略错误继续
    print("ignore 错误读取 ->", path.read_text(encoding="utf-8", errors="ignore"))


def main() -> None:
    base = Path(__file__).resolve().parent
    txt = base / "fruits.txt"
    write_lines(txt)
    print("== 逐行读取 ==")
    read_line_by_line(txt)
    print("\n== 分块读取 ==")
    read_in_chunks(txt)
    print("\n== 错误处理 ==")
    handle_errors(base / "bad.txt")
    txt.unlink(missing_ok=True)
    (base / "bad.txt").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
