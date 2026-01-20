#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 02: Compact JSON line.

Task:
Implement compact_json_line(data) -> str using json.dumps with compact separators.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/Exercises/02_json_compact_line.py
"""

import json


def compact_json_line(data: object) -> str:
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    data = {"a": 1, "b": [2, 3]}
    check("compact", compact_json_line(data), '{"a":1,"b":[2,3]}')


if __name__ == "__main__":
    main()
