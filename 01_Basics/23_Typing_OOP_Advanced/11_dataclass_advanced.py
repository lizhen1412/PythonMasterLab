#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 11: Advanced dataclass options.
Author: Lambert

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/11_dataclass_advanced.py
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError, dataclass, field


@dataclass(frozen=True, order=True, slots=True)
class Task:
    priority: int
    name: str = field(compare=False)
    tags: list[str] = field(default_factory=list, compare=False)


def main() -> None:
    tasks = [
        Task(2, "write"),
        Task(1, "read", tags=["short"]),
        Task(3, "test"),
    ]
    print("sorted ->", sorted(tasks))

    try:
        tasks[0].name = "edit"  # type: ignore[misc]
    except FrozenInstanceError as exc:
        print("frozen ->", exc)


if __name__ == "__main__":
    main()