#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 04: Read config with fallback.

Task:
Implement get_port(text, section, option, default) -> int.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/Exercises/04_configparser_get.py
"""

import configparser


def get_port(text: str, section: str, option: str, default: int) -> int:
    config = configparser.ConfigParser()
    config.read_string(text)
    if config.has_option(section, option):
        return config.getint(section, option)
    return default


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    text = """
    [db]
    port = 5432
    """
    check("exists", get_port(text, "db", "port", 3306), 5432)
    check("missing", get_port(text, "db", "missing", 3306), 3306)


if __name__ == "__main__":
    main()
