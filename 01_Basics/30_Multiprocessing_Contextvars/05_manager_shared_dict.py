#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: Manager shared dict.

Run:
    python3 01_Basics/30_Multiprocessing_Contextvars/05_manager_shared_dict.py
"""

import multiprocessing as mp


def set_value(shared, key: str, value: int) -> None:
    shared[key] = value


def main() -> None:
    with mp.Manager() as manager:
        shared = manager.dict()
        procs = [
            mp.Process(target=set_value, args=(shared, "a", 1)),
            mp.Process(target=set_value, args=(shared, "b", 2)),
        ]
        for p in procs:
            p.start()
        for p in procs:
            p.join()

        print("shared ->", dict(shared))


if __name__ == "__main__":
    main()
