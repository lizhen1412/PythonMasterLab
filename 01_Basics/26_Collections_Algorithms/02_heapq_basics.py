#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 02: heapq basics.
Author: Lambert

Run:
    python3 01_Basics/26_Collections_Algorithms/02_heapq_basics.py
"""

import heapq


def main() -> None:
    data = [5, 1, 3, 7, 2]
    heapq.heapify(data)
    print("heapified ->", data)

    heapq.heappush(data, 0)
    print("after push 0 ->", data)
    print("heappop ->", heapq.heappop(data))
    print("heap now ->", data)

    nums = [10, 4, 8, 1, 6, 9]
    print("nsmallest(3) ->", heapq.nsmallest(3, nums))
    print("nlargest(2) ->", heapq.nlargest(2, nums))

    print("\npriority queue with (priority, item):")
    pq: list[tuple[int, str]] = []
    heapq.heappush(pq, (2, "low"))
    heapq.heappush(pq, (1, "high"))
    heapq.heappush(pq, (3, "later"))
    while pq:
        print(heapq.heappop(pq))


if __name__ == "__main__":
    main()