#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 16：HTTP 方法完整演示（PUT/PATCH/DELETE/HEAD/OPTIONS）。

要点：
- PUT：完整更新资源（幂等）
- PATCH：部分更新资源
- DELETE：删除资源
- HEAD：只获取响应头（无 body）
- OPTIONS：获取服务器支持的 HTTP 方法

运行：
    python3 02_Frameworks/03_Requests/16_http_methods.py
"""

from __future__ import annotations

import json

import requests


def demo_put() -> None:
    """PUT 请求：完整更新资源"""
    resp = requests.put(
        "https://httpbin.org/put",
        json={"name": "Alice", "age": 25, "city": "Beijing"},
        timeout=5,
    )
    print(f"PUT 状态码 -> {resp.status_code}")
    print(f"PUT 返回的 json 字段 -> {json.dumps(resp.json()['json'], ensure_ascii=False)}")


def demo_patch() -> None:
    """PATCH 请求：部分更新资源"""
    resp = requests.patch(
        "https://httpbin.org/patch",
        json={"age": 26},  # 只更新 age 字段
        timeout=5,
    )
    print(f"\nPATCH 状态码 -> {resp.status_code}")
    print(f"PATCH 返回的 json 字段 -> {json.dumps(resp.json()['json'], ensure_ascii=False)}")


def demo_delete() -> None:
    """DELETE 请求：删除资源"""
    resp = requests.delete("https://httpbin.org/delete", timeout=5)
    print(f"\nDELETE 状态码 -> {resp.status_code}")
    print(f"DELETE 返回数据 -> {json.dumps(resp.json(), ensure_ascii=False)}")


def demo_head() -> None:
    """HEAD 请求：只获取响应头，不下载 body"""
    resp = requests.head("https://httpbin.org/get", timeout=5)
    print(f"\nHEAD 状态码 -> {resp.status_code}")
    print(f"HEAD Content-Length -> {resp.headers.get('Content-Length')}")
    print(f"HEAD 有 body 吗 -> {len(resp.content) == 0}")


def demo_options() -> None:
    """OPTIONS 请求：获取服务器支持的 HTTP 方法"""
    resp = requests.options("https://httpbin.org/get", timeout=5)
    print(f"\nOPTIONS 状态码 -> {resp.status_code}")
    print(f"OPTIONS Allow 头 -> {resp.headers.get('Allow')}")


def main() -> None:
    demo_put()
    demo_patch()
    demo_delete()
    demo_head()
    demo_options()


if __name__ == "__main__":
    main()
