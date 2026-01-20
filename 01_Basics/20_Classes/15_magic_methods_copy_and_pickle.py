#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：拷贝与序列化（__copy__/__deepcopy__/__getstate__/__setstate__/__reduce__）。

你会学到：
1) copy.copy / copy.deepcopy 的自定义行为
2) pickle 使用 __getstate__/__setstate__
3) __reduce__ 自定义序列化方式

运行（在仓库根目录执行）：
    python3 01_Basics/20_Classes/15_magic_methods_copy_and_pickle.py
"""

from __future__ import annotations

import copy
import pickle


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


class Notebook:
    def __init__(self, title: str, pages: list[str]) -> None:
        self.title = title
        self.pages = list(pages)
        self.cached_len = len(self.pages)

    def __repr__(self) -> str:
        return f"Notebook(title={self.title!r}, pages={self.pages!r}, cached_len={self.cached_len})"

    def __copy__(self) -> "Notebook":
        return type(self)(self.title, self.pages)

    def __deepcopy__(self, memo) -> "Notebook":
        pages = copy.deepcopy(self.pages, memo)
        return type(self)(self.title, pages)

    def __getstate__(self) -> dict[str, object]:
        return {"title": self.title, "pages": self.pages}

    def __setstate__(self, state: dict[str, object]) -> None:
        self.title = state["title"]
        self.pages = list(state["pages"])
        self.cached_len = len(self.pages)


class Token:
    def __init__(self, raw: str) -> None:
        self.raw = raw

    def __repr__(self) -> str:
        return f"Token({self.raw!r})"

    def __reduce__(self):
        return (type(self), (self.raw,))


def main() -> None:
    show("1) copy / deepcopy")
    nb = Notebook("Ideas", ["p1", "p2"])
    shallow = copy.copy(nb)
    deep = copy.deepcopy(nb)
    nb.pages.append("p3")
    print("original ->", nb)
    print("shallow  ->", shallow)
    print("deep     ->", deep)

    show("2) pickle: __getstate__/__setstate__")
    data = pickle.dumps(nb)
    restored: Notebook = pickle.loads(data)
    print("restored ->", restored)

    show("3) __reduce__")
    token = Token("abc123")
    rebuilt = pickle.loads(pickle.dumps(token))
    print("rebuilt ->", rebuilt)


if __name__ == "__main__":
    main()
