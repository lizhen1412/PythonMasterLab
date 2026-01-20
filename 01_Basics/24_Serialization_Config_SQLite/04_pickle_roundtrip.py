#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 04: Pickle roundtrip and security warning.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/04_pickle_roundtrip.py
"""

import pickle


def main() -> None:
    data = {"nums": [1, 2, 3], "flag": True}

    blob = pickle.dumps(data)
    restored = pickle.loads(blob)

    print("pickle bytes length ->", len(blob))
    print("restored ->", restored)
    print("equal ->", restored == data)

    print("warning: never unpickle data from untrusted sources")


if __name__ == "__main__":
    main()
