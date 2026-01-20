#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 08：字符串 str（序列特性 + 高频文本方法）

你会学到：
1) str 也是序列：索引/切片/遍历/成员测试
2) str 不可变：不能修改单个字符
3) 高频方法：strip/split/join/replace/find/startswith/endswith/lower/upper

运行（在仓库根目录执行）：
    python3 01_Basics/12_Composite_Types/08_string_basics.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def main() -> None:
    s = "  Hello, Python  "

    show("1) 索引/切片/遍历")
    print("s.strip() ->", s.strip())
    t = s.strip()
    print("t[0] ->", t[0])
    print("t[-1] ->", t[-1])
    print("t[0:5] ->", t[0:5])
    print("'Py' in t ->", "Py" in t)
    print("chars:", [ch for ch in "abc"])

    show("2) 不可变：不能 s[0] = ...")
    try:
        t[0] = "X"  # type: ignore[misc]
    except TypeError as exc:
        print("TypeError:", exc)

    show("3) split / join")
    parts = t.split()
    print("split() ->", parts)
    print("'|'.join(parts) ->", "|".join(parts))

    show("4) replace / find / startswith / endswith")
    print("replace ->", t.replace("Python", "World"))
    print("find('Py') ->", t.find("Py"))
    print("startswith('Hello') ->", t.startswith("Hello"))
    print("endswith('on') ->", t.endswith("on"))

    show("5) 大小写")
    print("lower ->", "ABC".lower())
    print("upper ->", "abc".upper())


if __name__ == "__main__":
    main()

