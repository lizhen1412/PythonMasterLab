#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：函数化的名片管理系统（简化版）。

- 数据存储：内存 list[dict]，字段包含 name/phone/email/tags
- 功能：新增、查询（精确/模糊）、更新、删除、格式化打印
- 重点展示“用函数拆分职责与复用”，而不是交互细节
"""

from __future__ import annotations

from typing import Any, Iterable, Optional

Card = dict[str, Any]
CardBook = list[Card]


def create_card(name: str, phone: str, email: str, *, tags: Optional[list[str]] = None) -> Card:
    """构造一张名片（不会写入 book）。"""
    return {"name": name, "phone": phone, "email": email, "tags": tags or []}


def add_card(book: CardBook, card: Card) -> None:
    """添加名片，避免重复姓名。"""
    if any(existing["name"] == card["name"] for existing in book):
        raise ValueError(f"name '{card['name']}' already exists")
    book.append(card)


def list_cards(book: CardBook) -> None:
    """打印表格视图。"""
    if not book:
        print("[EMPTY] card book is empty.")
        return

    headers = ("Name", "Phone", "Email", "Tags")
    rows = [
        (
            card["name"],
            card["phone"],
            card["email"],
            ", ".join(card.get("tags", [])),
        )
        for card in book
    ]
    print_table(headers, rows)


def find_cards(book: CardBook, keyword: str) -> list[Card]:
    """模糊查找（姓名或邮箱包含 keyword）。"""
    keyword_lower = keyword.lower()
    return [
        card
        for card in book
        if keyword_lower in card["name"].lower() or keyword_lower in card["email"].lower()
    ]


def update_card(card: Card, *, phone: Optional[str] = None, email: Optional[str] = None, tags: Optional[Iterable[str]] = None) -> None:
    """原地更新字段；None 表示保持不变。"""
    if phone is not None:
        card["phone"] = phone
    if email is not None:
        card["email"] = email
    if tags is not None:
        card["tags"] = list(tags)


def remove_card(book: CardBook, name: str) -> bool:
    """按姓名删除，返回是否删除成功。"""
    for idx, card in enumerate(book):
        if card["name"] == name:
            del book[idx]
            return True
    return False


def print_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> None:
    """简单的等宽表格渲染。"""
    widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(str(cell)))

    def render_row(row: tuple[str, ...]) -> str:
        return " | ".join(f"{str(cell):<{widths[i]}}" for i, cell in enumerate(row))

    line = "-+-".join("-" * w for w in widths)
    print(render_row(headers))
    print(line)
    for row in rows:
        print(render_row(row))


def demo_flow() -> None:
    """演示一次完整增删改查流程（非交互）。"""
    book: CardBook = [
        create_card("Alice", "123-456", "alice@example.com", tags=["friend"]),
        create_card("Bob", "555-000", "bob@example.com", tags=["work"]),
    ]
    print("初始数据：")
    list_cards(book)

    print("\n新增 Charlie：")
    add_card(book, create_card("Charlie", "999-888", "charlie@example.com", tags=["vip", "friend"]))
    list_cards(book)

    print("\n模糊搜索 'ali'：")
    matches = find_cards(book, "ali")
    list_cards(matches)

    print("\n更新 Bob 电话与标签：")
    bob = find_cards(book, "bob")[0]
    update_card(bob, phone="010-0000", tags=["work", "team"])
    list_cards(book)

    print("\n删除 Alice：")
    removed = remove_card(book, "Alice")
    print("删除成功?", removed)
    list_cards(book)


def main() -> None:
    demo_flow()


if __name__ == "__main__":
    main()
