#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercises index: Typing and OOP Advanced.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_parse_int_optional.py", "Optional return for parsing"),
    ("03_generic_first_or.py", "TypeVar-based generic helper"),
    ("04_protocol_total_size.py", "Protocol with __len__"),
    ("05_typeddict_format_user.py", "TypedDict with optional field"),
    ("06_typeguard_str_list.py", "TypeGuard for list[str]"),
    ("07_dataclass_frozen_point.py", "Frozen dataclass point"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Exercise files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
