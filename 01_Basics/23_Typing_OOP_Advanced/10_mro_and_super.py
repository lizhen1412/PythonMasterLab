#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 10: MRO and cooperative super().
Author: Lambert

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/10_mro_and_super.py
"""

from __future__ import annotations


class A:
    def ping(self, trail: list[str]) -> None:
        trail.append("A")


class B(A):
    def ping(self, trail: list[str]) -> None:
        trail.append("B")
        super().ping(trail)


class C(A):
    def ping(self, trail: list[str]) -> None:
        trail.append("C")
        super().ping(trail)


class D(B, C):
    def ping(self, trail: list[str]) -> None:
        trail.append("D")
        super().ping(trail)


def main() -> None:
    d = D()
    trail: list[str] = []
    d.ping(trail)
    print("trail ->", trail)
    print("MRO ->", [cls.__name__ for cls in D.mro()])


if __name__ == "__main__":
    main()