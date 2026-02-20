#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: math module basics.
Author: Lambert

Run:
    python3 01_Basics/28_Math_Statistics/02_math_basics.py
"""

import math


def main() -> None:
    print("sqrt(9) ->", math.sqrt(9))
    print("log10(1000) ->", math.log10(1000))
    print("sin(pi/2) ->", math.sin(math.pi / 2))
    print("pi ->", math.pi)

    x = 0.1 + 0.2
    print("isclose(0.1+0.2, 0.3) ->", math.isclose(x, 0.3))


if __name__ == "__main__":
    main()