#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: multiprocessing.Process basics.
Author: Lambert

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/02_multiprocessing_process_basics.py
"""

import multiprocessing as mp


def worker(name: str) -> None:
    print("worker ->", name)


def main() -> None:
    proc = mp.Process(target=worker, args=("demo",))
    proc.start()
    proc.join()
    print("exitcode ->", proc.exitcode)


if __name__ == "__main__":
    main()