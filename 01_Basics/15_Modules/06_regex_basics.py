#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：正则表达式基础（re 模块）。
Author: Lambert

- compile/search/match/findall
- 分组与命名分组
- 替换 sub、分割 split
"""

from __future__ import annotations

import re
from typing import Iterable


def search_basic(text: str) -> None:
    pattern = re.compile(r"(P|p)ython (?P<version>3\.\d+)")
    match = pattern.search(text)
    if match:
        print("找到 ->", match.group(0))
        print("版本 ->", match.group("version"))
        print("span ->", match.span())
    else:
        print("未找到匹配")


def findall_emails(text: str) -> None:
    email_pattern = re.compile(r"[\\w.]+@[\\w.-]+")
    print("提取到的邮箱 ->", email_pattern.findall(text))


def substitute(text: str) -> None:
    digits = re.compile(r"\\d+")
    masked = digits.sub("***", text)
    print("替换数字 ->", masked)


def split_and_iter(text: str) -> None:
    parts = re.split(r"[;,\\s]+", text.strip())
    cleaned = [p for p in parts if p]
    print("分割结果 ->", cleaned)


def main() -> None:
    search_basic("I love Python 3.11 and also python 3.9.")
    findall_emails("Contact us: dev@example.com, ops@test.cn")
    substitute("Order 12345 has amount 678.90")
    split_and_iter("apple, banana; cherry  durian")


if __name__ == "__main__":
    main()