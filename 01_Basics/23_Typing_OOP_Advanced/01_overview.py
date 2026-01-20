#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 01: Typing and OOP Advanced index.

Run (from repo root):
    python3 01_Basics/23_Typing_OOP_Advanced/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_typing_unions_optional_literal.py", "Union/Optional/Literal basics"),
    ("03_typing_typevar_generics.py", "TypeVar and generics"),
    ("04_typing_protocols_structural.py", "Protocol and structural typing"),
    ("05_typing_typeddict_newtype.py", "TypedDict and NewType"),
    ("06_typing_callable_paramspec.py", "Callable and ParamSpec"),
    ("07_typing_typeguard_self.py", "TypeGuard and Self"),
    ("08_future_annotations_and_get_type_hints.py", "__future__ annotations and get_type_hints"),
    ("09_abc_and_abstractmethod.py", "abc and abstract methods"),
    ("10_mro_and_super.py", "MRO and cooperative super()"),
    ("11_dataclass_advanced.py", "dataclass advanced options"),
    ("12_chapter_summary.py", "Chapter summary"),
    ("Exercises/01_overview.py", "Exercises index"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"Directory: {here}")
    print("Lesson files:")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()
