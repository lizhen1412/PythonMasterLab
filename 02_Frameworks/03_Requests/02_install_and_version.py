#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 02：安装与版本检查（requests 2.32.3）。

运行：
    python3 02_Frameworks/03_Requests/02_install_and_version.py
"""

from __future__ import annotations

import requests

EXPECTED = "2.32.3"


def main() -> None:
    print("requests version ->", requests.__version__)
    if requests.__version__ != EXPECTED:
        print(f"警告：本章基于 {EXPECTED}，当前为 {requests.__version__}")

    resp = requests.get("https://httpbin.org/get", timeout=5)
    print("示例请求（httpbin.org）状态码 ->", resp.status_code)


if __name__ == "__main__":
    main()
