#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: contextmanager timer.

Task:
Implement timer() context manager that reports elapsed seconds.

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/02_timer_context.py
"""

from contextlib import contextmanager
from time import perf_counter


@contextmanager
def timer():
    start = perf_counter()
    result = {"elapsed": 0.0}
    try:
        yield result
    finally:
        result["elapsed"] = perf_counter() - start


def check(label: str, ok: bool) -> None:
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")


def main() -> None:
    with timer() as info:
        _ = sum(range(1000))
    check("elapsed", info["elapsed"] >= 0.0)


if __name__ == "__main__":
    main()
