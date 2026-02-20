#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: contextmanager basics.
Author: Lambert

Run:
    python3 01_Basics/29_Contextlib_Assert_Pdb/02_contextmanager_basics.py
"""

from contextlib import contextmanager


@contextmanager
def labeled(label: str):
    print("enter ->", label)
    try:
        yield
    finally:
        print("exit ->", label)


def main() -> None:
    with labeled("demo"):
        print("inside")


if __name__ == "__main__":
    main()