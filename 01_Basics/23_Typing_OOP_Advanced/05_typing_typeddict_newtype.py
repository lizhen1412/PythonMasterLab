#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 05: TypedDict and NewType.
Author: Lambert

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/05_typing_typeddict_newtype.py
"""

from __future__ import annotations

from typing import NewType, TypedDict

UserId = NewType("UserId", int)


class User(TypedDict):
    id: UserId
    name: str
    active: bool


def format_user(user: User) -> str:
    return f"#{int(user['id'])} {user['name']} active={user['active']}"


def main() -> None:
    u: User = {"id": UserId(1001), "name": "Alice", "active": True}
    print(format_user(u))
    print("UserId is int at runtime ->", isinstance(u["id"], int))


if __name__ == "__main__":
    main()