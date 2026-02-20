#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：重定向与 history。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/10_redirects_and_history.py
"""

from __future__ import annotations

import requests


def main() -> None:
    resp = requests.get(
        "https://httpbin.org/redirect-to",
        params={"url": "https://httpbin.org/get"},
        timeout=5,
    )
    print("跟随重定向状态码 ->", resp.status_code)
    print("最终 URL ->", resp.url)
    print("history 长度 ->", len(resp.history))
    if resp.history:
        first = resp.history[0]
        print("首个重定向 ->", first.status_code, first.headers.get("Location"))

    resp_no_follow = requests.get(
        "https://httpbin.org/redirect-to",
        params={"url": "https://httpbin.org/get"},
        allow_redirects=False,
        timeout=5,
    )
    print("\n不跟随重定向状态码 ->", resp_no_follow.status_code)
    print("Location 头 ->", resp_no_follow.headers.get("Location"))


if __name__ == "__main__":
    main()