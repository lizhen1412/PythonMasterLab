#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 12: Chapter summary.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/12_chapter_summary.py
"""


def main() -> None:
    points = [
        "Union/Optional/Literal express precise API types",
        "TypeVar enables generic helpers and containers",
        "Protocol defines structural typing contracts",
        "TypedDict models dict-shaped data; NewType adds semantic meaning",
        "ParamSpec preserves decorator signatures",
        "TypeGuard narrows types at runtime checks",
        "Self improves fluent method typing",
        "__future__ annotations help with forward references",
        "abc enforces abstract methods",
        "MRO + super() require cooperative design",
        "dataclass options: frozen/slots/order/field",
    ]
    print("== Key points ==")
    for item in points:
        print("-", item)


if __name__ == "__main__":
    main()
