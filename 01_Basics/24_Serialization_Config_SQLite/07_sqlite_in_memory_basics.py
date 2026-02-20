#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 07: sqlite3 in-memory basics.
Author: Lambert

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/07_sqlite_in_memory_basics.py
"""

import sqlite3


def main() -> None:
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, name TEXT)")
    cur.executemany("INSERT INTO user (name) VALUES (?)", [("Alice",), ("Bob",)])

    cur.execute("SELECT id, name FROM user ORDER BY id")
    rows = cur.fetchall()
    print("rows ->", rows)

    conn.close()


if __name__ == "__main__":
    main()