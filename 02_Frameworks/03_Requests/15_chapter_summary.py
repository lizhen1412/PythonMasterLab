#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：本章总结。

运行：
    python3 02_Frameworks/03_Requests/15_chapter_summary.py
"""

from __future__ import annotations


def main() -> None:
    points = [
        "Request/PreparedRequest：先构建再发送，便于检查最终 URL/头",
        "响应属性：status_code/headers/text/content/json/encoding",
        "POST：data 生成表单，json 自动编码为 application/json",
        "超时与异常：Timeout/ConnectionError/HTTPError，结合 raise_for_status",
        "Session：连接复用、默认头、Cookie 持久化",
        "重定向：history/allow_redirects 控制跳转",
        "流式下载：stream=True + iter_content 节省内存",
        "上传与认证：files multipart、Basic Auth",
        "重试：HTTPAdapter + Retry 配置总次数、后退时间、重试状态码",
    ]
    print("Requests 本章要点：")
    for idx, item in enumerate(points, 1):
        print(f"{idx}. {item}")


if __name__ == "__main__":
    main()
