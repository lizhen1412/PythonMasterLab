#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: JSON dumps/loads basics.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/02_json_dumps_loads.py
"""

import json


def main() -> None:
    data = {"user": {"name": "Alice", "age": 20}, "tags": ["python", "json"]}

    text = json.dumps(data, ensure_ascii=False, indent=2)
    print("dumps ->")
    print(text)

    decoded = json.loads(text)
    print("loads ->", decoded)

    compact = json.dumps(data, separators=(",", ":"))
    print("compact ->", compact)


if __name__ == "__main__":
    main()
