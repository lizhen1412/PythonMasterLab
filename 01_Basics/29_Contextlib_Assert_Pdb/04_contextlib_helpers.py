#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: contextlib helpers.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/04_contextlib_helpers.py
"""

from contextlib import redirect_stdout, suppress
from io import StringIO


def main() -> None:
    with suppress(ValueError):
        int("x")
        print("this will not run")

    buf = StringIO()
    with redirect_stdout(buf):
        print("captured")
    print("stdout ->", buf.getvalue().strip())


if __name__ == "__main__":
    main()
