#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: ExitStack usage.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/03_exitstack_basics.py
"""

from contextlib import ExitStack
from io import StringIO


def main() -> None:
    buf1 = StringIO()
    buf2 = StringIO()

    with ExitStack() as stack:
        stack.enter_context(buf1)
        stack.enter_context(buf2)
        buf1.write("one")
        buf2.write("two")
        print("inside ->", buf1.getvalue(), buf2.getvalue())

    print("closed ->", buf1.closed, buf2.closed)


if __name__ == "__main__":
    main()
