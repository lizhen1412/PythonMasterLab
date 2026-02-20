#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 08: __future__ annotations and get_type_hints.
Author: Lambert

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/08_future_annotations_and_get_type_hints.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import get_type_hints


@dataclass
class Node:
    value: int
    next: Node | None = None


def main() -> None:
    node = Node(1, Node(2))
    print("node ->", node)

    hints = get_type_hints(Node)
    print("type hints ->", hints)


if __name__ == "__main__":
    main()