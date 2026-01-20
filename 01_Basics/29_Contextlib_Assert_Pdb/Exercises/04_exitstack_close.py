#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: ExitStack closes resources.

Task:
Implement collect_texts(texts) -> tuple[list[str], list[bool]].
Use ExitStack to close StringIO buffers.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/04_exitstack_close.py
"""

from contextlib import ExitStack
from io import StringIO


def collect_texts(texts: list[str]) -> tuple[list[str], list[bool]]:
    buffers: list[StringIO] = [StringIO() for _ in texts]
    with ExitStack() as stack:
        for buf in buffers:
            stack.enter_context(buf)
        for buf, text in zip(buffers, texts):
            buf.write(text)
        values = [buf.getvalue() for buf in buffers]
    closed = [buf.closed for buf in buffers]
    return values, closed


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    values, closed = collect_texts(["a", "b"])
    check("values", values, ["a", "b"])
    check("closed", closed, [True, True])


if __name__ == "__main__":
    main()
