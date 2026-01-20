#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: Union / Optional / Literal basics.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/02_typing_unions_optional_literal.py
"""

from __future__ import annotations

from typing import Literal


def parse_int(text: str) -> int | None:
    """Return int if text is valid, otherwise None."""
    try:
        return int(text)
    except ValueError:
        return None


Status = Literal["ok", "error", "unknown"]


def status_from_code(code: int) -> Status:
    if code == 200:
        return "ok"
    if code >= 500:
        return "error"
    return "unknown"


def main() -> None:
    print("parse_int('42') ->", parse_int("42"))
    print("parse_int('x') ->", parse_int("x"))

    print("status_from_code(200) ->", status_from_code(200))
    print("status_from_code(503) ->", status_from_code(503))
    print("status_from_code(404) ->", status_from_code(404))


if __name__ == "__main__":
    main()
