#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lesson 09: abc and abstract methods.

Run:
    python3 01_Basics/23_Typing_OOP_Advanced/09_abc_and_abstractmethod.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, key: str, value: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self, key: str) -> str | None:
        raise NotImplementedError


class MemoryStorage(Storage):
    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def save(self, key: str, value: str) -> None:
        self._data[key] = value

    def load(self, key: str) -> str | None:
        return self._data.get(key)


def main() -> None:
    store = MemoryStorage()
    store.save("token", "abc")
    print("load ->", store.load("token"))

    try:
        Storage()  # type: ignore[abstract]
    except TypeError as exc:
        print("cannot instantiate abstract class ->", exc)


if __name__ == "__main__":
    main()
