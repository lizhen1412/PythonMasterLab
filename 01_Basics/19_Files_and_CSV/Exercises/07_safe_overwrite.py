#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 07：安全写入：临时文件替换原文件。
"""

from __future__ import annotations

import tempfile
from pathlib import Path


def safe_write(path: Path, content: str) -> None:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=path.parent, newline="") as tmp:
        tmp_path = Path(tmp.name)
        tmp.write(content)
    tmp_path.replace(path)


def main() -> None:
    base = Path(__file__).resolve().parent
    target = base / "target.txt"
    safe_write(target, "new content")
    print("written ->", target.read_text(encoding="utf-8"))
    target.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
