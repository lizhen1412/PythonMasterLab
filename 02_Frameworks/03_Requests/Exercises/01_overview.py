#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：requests 2.32.3。
Author: Lambert

运行方式（在仓库根目录执行）：
    python3 02_Frameworks/03_Requests/Exercises/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    # 基础练习 (02-09)
    ("02_get_with_params.py", "GET 请求带查询参数"),
    ("03_post_json.py", "POST JSON 数据"),
    ("04_headers_auth.py", "自定义头和 Basic Auth"),
    ("05_error_handling.py", "错误处理和状态码检查"),
    ("06_session_retry.py", "Session 和重试策略"),
    ("07_file_download.py", "文件下载（流式）"),
    ("08_file_upload.py", "文件上传"),
    ("09_cookie_jar.py", "Cookie 持久化"),
    # 进阶练习 (10-13)
    ("10_rest_client.py", "REST API 客户端"),
    ("11_proxy_config.py", "代理配置"),
    ("12_timeout_retry.py", "超时和重试进阶"),
    ("13_async_requests.py", "AsyncIO 集成"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()