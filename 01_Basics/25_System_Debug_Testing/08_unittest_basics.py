#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 08: unittest basics.
Author: Lambert

Run:
    python3 01_Basics/25_System_Debug_Testing/08_unittest_basics.py
"""

import unittest


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


class TestClamp(unittest.TestCase):
    def test_middle(self) -> None:
        self.assertEqual(clamp(5, 1, 10), 5)

    def test_low(self) -> None:
        self.assertEqual(clamp(-1, 0, 10), 0)

    def test_high(self) -> None:
        self.assertEqual(clamp(99, 0, 10), 10)


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClamp)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("all ok ->", result.wasSuccessful())


if __name__ == "__main__":
    main()