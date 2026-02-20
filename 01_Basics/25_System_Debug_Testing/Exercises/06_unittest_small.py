#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 06: Small unittest example.
Author: Lambert

Task:
Implement is_even(n) and test it with unittest.

Run:
    python3 01_Basics/25_System_Debug_Testing/Exercises/06_unittest_small.py
"""

import unittest


def is_even(n: int) -> bool:
    return n % 2 == 0


class TestIsEven(unittest.TestCase):
    def test_even(self) -> None:
        self.assertTrue(is_even(2))

    def test_odd(self) -> None:
        self.assertFalse(is_even(3))


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestIsEven)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("all ok ->", result.wasSuccessful())


if __name__ == "__main__":
    main()