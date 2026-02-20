#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: getenv with default.
Author: Lambert

Task:
Implement get_env(name, default) -> str.

Run:
    python3 01_Basics/25_System_Debug_Testing/Exercises/02_get_env_default.py
"""

import os


def get_env(name: str, default: str) -> str:
    return os.getenv(name, default)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("missing", get_env("_NOT_SET_", "fallback"), "fallback")


if __name__ == "__main__":
    main()