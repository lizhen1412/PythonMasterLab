#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 14：HTTPAdapter + Retry（简单重试策略）。

运行：
    python3 02_Frameworks/03_Requests/14_retries_and_adapter.py
"""

from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def main() -> None:
    retry = Retry(
        total=2,
        backoff_factor=0.2,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )
    adapter = HTTPAdapter(max_retries=retry)

    session = requests.Session()
    session.mount("https://", adapter)

    resp = session.get("https://httpbin.org/status/503", timeout=5)
    print("最终状态码 ->", resp.status_code)

    history = getattr(resp.raw, "retries", None)
    if history:
        retry_history = getattr(history, "history", [])
        print("重试次数（包含首次） ->", len(retry_history) + 1)
    else:
        print("未找到 retries 对象（可能 urllib3 版本差异）")


if __name__ == "__main__":
    main()
