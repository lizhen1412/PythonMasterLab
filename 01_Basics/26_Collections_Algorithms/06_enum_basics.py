#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 06: Enum, IntEnum, Flag.

Run:
    python3 01_Basics/26_Collections_Algorithms/06_enum_basics.py
"""

from enum import Enum, Flag, IntEnum, auto


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Level(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Perm(Flag):
    READ = auto()
    WRITE = auto()
    EXEC = auto()


def main() -> None:
    c = Color.RED
    print("color ->", c, c.value)

    level = Level.HIGH
    print("level ->", level, int(level))

    perm = Perm.READ | Perm.WRITE
    print("perm ->", perm)
    print("has READ ->", Perm.READ in perm)
    print("has EXEC ->", Perm.EXEC in perm)


if __name__ == "__main__":
    main()
