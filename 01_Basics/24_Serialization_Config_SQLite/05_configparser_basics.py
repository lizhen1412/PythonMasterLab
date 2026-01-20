#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: ConfigParser basics.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/05_configparser_basics.py
"""

import configparser


def main() -> None:
    text = """
    [app]
    debug = true
    retries = 3

    [db]
    host = localhost
    port = 5432
    """

    config = configparser.ConfigParser()
    config.read_string(text)

    print("debug ->", config.getboolean("app", "debug"))
    print("retries ->", config.getint("app", "retries"))
    print("db.host ->", config.get("db", "host"))
    print("db.port ->", config.getint("db", "port"))


if __name__ == "__main__":
    main()
