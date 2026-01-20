#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Run Python and capture output.

Task:
Implement run_echo(text) -> str using subprocess.run and sys.executable.

Run:
    python3 01_Basics/25_System_Debug_Testing/Exercises/03_subprocess_capture.py
"""

import subprocess
import sys


def run_echo(text: str) -> str:
    cmd = [sys.executable, "-c", f"print({text!r})"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("echo", run_echo("hello"), "hello")


if __name__ == "__main__":
    main()
