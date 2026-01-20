#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 03: File-like JSON and custom encoder.

Run:
    python3 01_Basics/24_Serialization_Config_SQLite/03_json_file_like_custom_encoder.py
"""

import json
from io import StringIO


def encode_default(obj: object):
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"not JSON serializable: {type(obj).__name__}")


def main() -> None:
    data = {"items": {"a", "b", "c"}}

    buf = StringIO()
    json.dump(data, buf, default=encode_default)
    text = buf.getvalue()
    print("json.dump ->", text)

    decoded = json.loads(text)
    print("decoded ->", decoded)


if __name__ == "__main__":
    main()
