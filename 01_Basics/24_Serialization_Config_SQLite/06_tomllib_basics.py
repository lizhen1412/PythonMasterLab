#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: TOML parsing with tomllib (Python 3.11+).

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/06_tomllib_basics.py
"""

import tomllib


def main() -> None:
    text = """
    title = "Example"

    [owner]
    name = "Tom"
    active = true

    [database]
    ports = [8001, 8001, 8002]
    """

    data = tomllib.loads(text)
    print("data ->", data)
    print("owner.name ->", data["owner"]["name"])


if __name__ == "__main__":
    main()
