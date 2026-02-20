#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：POST 表单 vs JSON（httpbin.org）。
Author: Lambert

运行：
    python3 02_Frameworks/03_Requests/05_post_form_vs_json.py
"""

from __future__ import annotations

import json

import requests


def main() -> None:
    form_resp = requests.post(
        "https://httpbin.org/post",
        data={"name": "alice", "age": "20"},
        timeout=5,
    )
    json_resp = requests.post(
        "https://httpbin.org/post",
        json={"name": "alice", "age": 20},
        timeout=5,
    )

    print("表单 Content-Type ->", form_resp.json()["headers"].get("Content-Type"))
    print("表单服务器看到的 form 字段 ->", json.dumps(form_resp.json()["form"], ensure_ascii=False))

    print("\nJSON Content-Type ->", json_resp.json()["headers"].get("Content-Type"))
    print("JSON 服务器看到的 json 字段 ->", json.dumps(json_resp.json()["json"], ensure_ascii=False))


if __name__ == "__main__":
    main()