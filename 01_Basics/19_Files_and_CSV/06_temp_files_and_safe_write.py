#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：tempfile、临时写后替换（安全写入模式）。
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Iterable


def safe_write(target: Path, lines: Iterable[str]) -> None:
    """
    先写临时文件，再替换目标文件，减少部分写入损坏的风险。
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=target.parent, newline="") as tmp:
        tmp_path = Path(tmp.name)
        for line in lines:
            tmp.write(line + "\n")
    tmp_path.replace(target)


def main() -> None:
    base = Path(__file__).resolve().parent
    target = base / "safe_output.txt"
    safe_write(target, ["line1", "line2", "line3"])
    print("safe_write 写入完成 ->", target)
    print("内容 ->", target.read_text(encoding="utf-8"))
    target.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
