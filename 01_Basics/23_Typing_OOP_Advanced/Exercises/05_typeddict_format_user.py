#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 05: TypedDict with optional field.

Task:
Define User TypedDict with name/age and optional nickname.
Implement format_user(user) -> str.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/05_typeddict_format_user.py
"""

from __future__ import annotations

from typing import NotRequired, TypedDict


class User(TypedDict):
    name: str
    age: int
    nickname: NotRequired[str]


def format_user(user: User) -> str:
    nick = f" ({user['nickname']})" if "nickname" in user else ""
    return f"{user['name']}{nick}, age={user['age']}"


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    u1: User = {"name": "Alice", "age": 20}
    u2: User = {"name": "Bob", "age": 30, "nickname": "B"}
    check("no nick", format_user(u1), "Alice, age=20")
    check("with nick", format_user(u2), "Bob (B), age=30")


if __name__ == "__main__":
    main()
