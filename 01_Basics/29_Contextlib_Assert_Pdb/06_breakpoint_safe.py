#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: Safe breakpoint usage.
Author: Lambert

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/06_breakpoint_safe.py
"""

import os


def main() -> None:
    print("PYTHONBREAKPOINT (before) ->", os.getenv("PYTHONBREAKPOINT"))

    os.environ["PYTHONBREAKPOINT"] = "0"
    print("PYTHONBREAKPOINT (after) ->", os.getenv("PYTHONBREAKPOINT"))

    print("calling breakpoint() (disabled)")
    breakpoint()
    print("after breakpoint")


if __name__ == "__main__":
    main()