#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 08: sqlite3 row_factory and parameterized queries.
Author: Lambert

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/08_sqlite_row_factory_and_params.py
"""

import sqlite3


def main() -> None:
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("CREATE TABLE item (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur.executemany(
        "INSERT INTO item (name, price) VALUES (?, ?)",
        [("pen", 1.2), ("book", 9.5), ("bag", 30.0)],
    )

    min_price = 5.0
    cur.execute("SELECT id, name, price FROM item WHERE price >= ?", (min_price,))
    for row in cur.fetchall():
        print(dict(row))

    conn.close()


if __name__ == "__main__":
    main()