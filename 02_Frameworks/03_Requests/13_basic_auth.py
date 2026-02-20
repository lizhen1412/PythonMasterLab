#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 13：Basic Auth。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/13_basic_auth.py
"""

from __future__ import annotations

import requests


def main() -> None:
    ok = requests.get(
        "https://httpbin.org/basic-auth/user/pass",
        auth=("user", "pass"),
        timeout=5,
    )
    print("正确凭据状态码 ->", ok.status_code, "返回 ->", ok.json())

    bad = requests.get(
        "https://httpbin.org/basic-auth/user/pass",
        auth=("user", "wrong"),
        timeout=5,
    )
    print("错误凭据状态码 ->", bad.status_code)


if __name__ == "__main__":
    main()