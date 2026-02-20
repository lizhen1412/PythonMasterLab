#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：文件上传 multipart/form-data。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/12_upload_files_multipart.py
"""

from __future__ import annotations

import json

import requests


def main() -> None:
    files = {
        "file": ("demo.txt", b"hello requests", "text/plain"),
    }
    resp = requests.post("https://httpbin.org/post", files=files, timeout=5)
    data = resp.json()
    print("服务器看到的 files 字段 ->", json.dumps(data["files"], ensure_ascii=False))
    print("服务器看到的 form 字段 ->", json.dumps(data["form"], ensure_ascii=False))


if __name__ == "__main__":
    main()