#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 11：流式下载与 iter_content。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/11_streaming_download.py
"""

from __future__ import annotations

import requests


def main() -> None:
    with requests.get("https://httpbin.org/stream/5", stream=True, timeout=5) as resp:
        print("状态码 ->", resp.status_code)
        chunks: list[bytes] = []
        for chunk in resp.iter_content(chunk_size=16):
            if not chunk:
                continue
            chunks.append(chunk)
            print("收到分块 ->", chunk)

        joined = b"".join(chunks)
        print("合并后总长度 ->", len(joined))


if __name__ == "__main__":
    main()