#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：raise_for_status 与状态码判断。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/08_raise_for_status.py
"""

from __future__ import annotations

import requests


def main() -> None:
    ok_resp = requests.get("https://httpbin.org/status/204", timeout=5)
    print("204 响应 ->", ok_resp.status_code)
    ok_resp.raise_for_status()
    print("204 raise_for_status -> 没有异常")

    try:
        bad_resp = requests.get("https://httpbin.org/status/404", timeout=5)
        print("404 响应 ->", bad_resp.status_code)
        bad_resp.raise_for_status()
    except requests.HTTPError as exc:
        print("捕获 HTTPError ->", type(exc).__name__, exc)


if __name__ == "__main__":
    main()