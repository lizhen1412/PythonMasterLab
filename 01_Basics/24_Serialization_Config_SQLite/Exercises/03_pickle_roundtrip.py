#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 03: Pickle roundtrip.
Author: Lambert

Task:
Implement roundtrip(obj) -> obj using pickle.dumps/loads.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/Exercises/03_pickle_roundtrip.py
"""

import pickle


def roundtrip(obj: object) -> object:
    return pickle.loads(pickle.dumps(obj))


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    data = {"x": [1, 2], "y": True}
    check("roundtrip", roundtrip(data), data)


if __name__ == "__main__":
    main()