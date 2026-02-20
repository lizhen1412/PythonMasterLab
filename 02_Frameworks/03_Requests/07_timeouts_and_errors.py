#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 07：超时与连接错误。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/07_timeouts_and_errors.py
"""

from __future__ import annotations

import requests


def demo_timeout() -> None:
    try:
        requests.get("https://httpbin.org/delay/3", timeout=1)
    except requests.Timeout as exc:
        print("捕获 Timeout ->", type(exc).__name__, exc)


def demo_connection_error() -> None:
    try:
        requests.get("https://invalid.example.invalid", timeout=3)
    except requests.ConnectionError as exc:
        print("捕获 ConnectionError ->", type(exc).__name__)


def main() -> None:
    demo_timeout()
    demo_connection_error()


if __name__ == "__main__":
    main()