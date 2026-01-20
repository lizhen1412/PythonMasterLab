#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 07: Frozen dataclass point.

Task:
Define a frozen dataclass Point(x, y) and a distance() method.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/Exercises/07_dataclass_frozen_point.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


def check(label: str, got: object, expected: object) -> None:
    ok = abs(got - expected) < 1e-9
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    check("(3,4)", Point(3, 4).distance(), 5.0)
    check("(0,0)", Point(0, 0).distance(), 0.0)


if __name__ == "__main__":
    main()
