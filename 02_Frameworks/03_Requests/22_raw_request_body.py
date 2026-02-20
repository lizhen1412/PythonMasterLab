#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 22：原始请求体与自定义 Content-Type。
Author: Lambert

要点：
- data 参数：发送字符串/字节作为请求体
- 自定义 Content-Type 头：控制请求体的解析方式
- 发送 XML、纯文本、自定义格式
- json 参数会自动设置 Content-Type

运行：
    python3 02_Frameworks/03_Requests/22_raw_request_body.py
"""

from __future__ import annotations

import json

import requests


def demo_raw_json_string() -> None:
    """演示手动发送 JSON 字符串"""
    payload = json.dumps({"name": "Alice", "age": 25})

    headers = {
        "Content-Type": "application/json; charset=utf-8",
    }

    resp = requests.post(
        "https://httpbin.org/post",
        data=payload,
        headers=headers,
        timeout=5,
    )

    print("=== 手动发送 JSON 字符串 ===")
    print(f"请求 Content-Type -> {resp.json()['headers']['Content-Type']}")
    print(f"服务器接收到的 data -> {resp.json()['data']}")


def demo_xml_body() -> None:
    """演示发送 XML 请求体"""
    xml_payload = """<?xml version="1.0" encoding="UTF-8"?>
<person>
    <name>Alice</name>
    <age>25</age>
</person>"""

    headers = {
        "Content-Type": "application/xml; charset=utf-8",
    }

    resp = requests.post(
        "https://httpbin.org/post",
        data=xml_payload,
        headers=headers,
        timeout=5,
    )

    print("\n=== 发送 XML 请求体 ===")
    print(f"请求 Content-Type -> {resp.json()['headers']['Content-Type']}")
    print(f"服务器接收到的 data (前100字符) -> {resp.json()['data'][:100]}")


def demo_plain_text() -> None:
    """演示发送纯文本请求体"""
    text_payload = "Hello, this is plain text!"

    headers = {
        "Content-Type": "text/plain; charset=utf-8",
    }

    resp = requests.post(
        "https://httpbin.org/post",
        data=text_payload,
        headers=headers,
        timeout=5,
    )

    print("\n=== 发送纯文本请求体 ===")
    print(f"请求 Content-Type -> {resp.json()['headers']['Content-Type']}")
    print(f"服务器接收到的 data -> {resp.json()['data']}")


def demo_bytes_body() -> None:
    """演示发送字节请求体"""
    bytes_payload = b"\x00\x01\x02\x03\x04\x05"

    headers = {
        "Content-Type": "application/octet-stream",
    }

    resp = requests.post(
        "https://httpbin.org/post",
        data=bytes_payload,
        headers=headers,
        timeout=5,
    )

    print("\n=== 发送字节请求体 ===")
    print(f"请求 Content-Type -> {resp.json()['headers']['Content-Type']}")
    print(f"服务器接收到的 data -> {resp.json()['data']}")


def demo_custom_content_type() -> None:
    """演示自定义 Content-Type"""
    custom_data = "custom_protocol_v1|key1=value1|key2=value2"

    headers = {
        "Content-Type": "application/vnd.example.v1+text",
    }

    resp = requests.post(
        "https://httpbin.org/post",
        data=custom_data,
        headers=headers,
        timeout=5,
    )

    print("\n=== 自定义 Content-Type ===")
    print(f"请求 Content-Type -> {resp.json()['headers']['Content-Type']}")
    print(f"服务器接收到的 data -> {resp.json()['data']}")


def demo_form_urlencoded() -> None:
    """演示 application/x-www-form-urlencoded"""
    form_data = {"name": "Alice", "age": "25"}

    # data 参数如果是 dict，默认使用 form-urlencoded
    resp = requests.post(
        "https://httpbin.org/post",
        data=form_data,
        timeout=5,
    )

    print("\n=== Form URL编码 ===")
    print(f"请求 Content-Type -> {resp.json()['headers']['Content-Type']}")
    print(f"服务器接收到的 form -> {resp.json()['form']}")


def demo_json_parameter_comparison() -> None:
    """对比 json 参数和手动设置"""
    print("\n=== json 参数 vs 手动设置 ===")

    # 方式1：使用 json 参数（推荐）
    resp1 = requests.post(
        "https://httpbin.org/post",
        json={"name": "Alice", "age": 25},
        timeout=5,
    )
    print(f"json 参数 Content-Type -> {resp1.json()['headers']['Content-Type']}")

    # 方式2：手动设置
    payload = json.dumps({"name": "Alice", "age": 25})
    headers = {"Content-Type": "application/json"}
    resp2 = requests.post(
        "https://httpbin.org/post",
        data=payload,
        headers=headers,
        timeout=5,
    )
    print(f"手动设置 Content-Type -> {resp2.json()['headers']['Content-Type']}")

    # 两种方式效果相同
    assert resp1.json()["data"] == resp2.json()["data"]
    print("两种方式发送的数据相同")


def demo_charset_encoding() -> None:
    """演示字符集编码"""
    chinese_text = "你好世界！"

    # 默认 UTF-8
    headers1 = {"Content-Type": "text/plain"}
    resp1 = requests.post(
        "https://httpbin.org/post",
        data=chinese_text,
        headers=headers1,
        timeout=5,
    )

    # 显式指定 UTF-8
    headers2 = {"Content-Type": "text/plain; charset=utf-8"}
    resp2 = requests.post(
        "https://httpbin.org/post",
        data=chinese_text,
        headers=headers2,
        timeout=5,
    )

    print("\n=== 字符集编码 ===")
    print(f"默认编码 -> {resp1.json()['headers'].get('Content-Type', '未指定')}")
    print(f"显式 UTF-8 -> {resp2.json()['headers']['Content-Type']}")
    print(f"接收到的数据 -> {resp2.json()['data']}")


def main() -> None:
    print("=== 原始请求体与自定义 Content-Type 演示 ===\n")
    demo_raw_json_string()
    demo_xml_body()
    demo_plain_text()
    demo_bytes_body()
    demo_custom_content_type()
    demo_form_urlencoded()
    demo_json_parameter_comparison()
    demo_charset_encoding()

    print("\n使用建议:")
    print("  - 发送 JSON 优先使用 json 参数")
    print("  - 发送 XML/文本使用 data + 自定义 Content-Type")
    print("  - 涉及非 ASCII 字符时建议显式指定 charset=utf-8")
    print("  - 自定义协议使用 vendor-specific MIME 类型 (application/vnd.*)")


if __name__ == "__main__":
    main()