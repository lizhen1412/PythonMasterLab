#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 06: Insert and count rows.
Author: Lambert

Task:
Implement insert_and_count(names) -> int using sqlite3 in-memory DB.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/Exercises/06_sqlite_insert_count.py
"""

import sqlite3


def insert_and_count(names: list[str]) -> int:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)")
    cur.executemany("INSERT INTO user (name) VALUES (?)", [(name,) for name in names])
    cur.execute("SELECT COUNT(*) FROM user")
    count = int(cur.fetchone()[0])
    conn.close()
    return count


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("count", insert_and_count(["a", "b", "c"]), 3)
    check("empty", insert_and_count([]), 0)


if __name__ == "__main__":
    main()