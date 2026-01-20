#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：捕获 FileNotFound/PermissionError。
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    missing = base / "missing.txt"
    try:
        missing.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        print("捕获 FileNotFoundError ->", exc)

    temp = base / "readonly.txt"
    temp.write_text("hi", encoding="utf-8")
    orig_mode = temp.stat().st_mode
    temp.chmod(0o444)
    try:
        temp.write_text("fail", encoding="utf-8")
    except PermissionError as exc:
        print("捕获 PermissionError ->", exc)
    finally:
        temp.chmod(orig_mode)
        temp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
