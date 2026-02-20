#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 09：为名片系统补充“按姓名模糊搜索”功能。
Author: Lambert

要求：
- 用函数封装：接受 card 列表与关键字，返回匹配结果
- 不区分大小写；命中姓名包含关键字即可
"""

from __future__ import annotations

from typing import Any, Iterable

Card = dict[str, Any]


def search_by_name(cards: Iterable[Card], keyword: str) -> list[Card]:
    key = keyword.lower()
    return [card for card in cards if key in card["name"].lower()]


def main() -> None:
    book = [
        {"name": "Alice", "phone": "123", "email": "alice@example.com"},
        {"name": "Bob", "phone": "555", "email": "bob@example.com"},
        {"name": "Charlie", "phone": "999", "email": "charlie@example.com"},
    ]

    matches = search_by_name(book, "ali")
    print("search 'ali' ->", [card["name"] for card in matches])

    matches = search_by_name(book, "BO")
    print("search 'BO' ->", [card["name"] for card in matches])


if __name__ == "__main__":
    main()