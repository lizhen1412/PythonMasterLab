#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：Session 复用与 Cookie。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/09_session_and_cookies.py
"""

from __future__ import annotations

import json

import requests


def main() -> None:
    session = requests.Session()
    session.headers.update({"User-Agent": "pythonmasterlab-requests-demo/1.0"})

    resp1 = session.get("https://httpbin.org/cookies", timeout=5)
    print("初始 cookies ->", json.dumps(resp1.json()["cookies"], ensure_ascii=False))

    session.get("https://httpbin.org/cookies/set/demo/123", timeout=5)
    resp2 = session.get("https://httpbin.org/cookies", timeout=5)
    print("设置后 cookies ->", json.dumps(resp2.json()["cookies"], ensure_ascii=False))


if __name__ == "__main__":
    main()