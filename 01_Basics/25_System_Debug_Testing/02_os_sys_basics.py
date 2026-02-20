#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: os/sys essentials.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/02_os_sys_basics.py
"""

import os
import sys


def main() -> None:
    print("cwd ->", os.getcwd())
    print("platform ->", sys.platform)
    print("python ->", sys.version_info[:3])
    print("argv ->", sys.argv)
    print("HOME ->", os.getenv("HOME"))
    print("PATH exists ->", os.getenv("PATH") is not None)


if __name__ == "__main__":
    main()