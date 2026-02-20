#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: subprocess basics.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/04_subprocess_basics.py
"""

import subprocess
import sys


def main() -> None:
    cmd = [sys.executable, "-c", "print('hello from subprocess')"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print("stdout ->", result.stdout.strip())
    print("returncode ->", result.returncode)


if __name__ == "__main__":
    main()