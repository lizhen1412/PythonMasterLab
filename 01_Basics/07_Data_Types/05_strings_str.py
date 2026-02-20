#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 05：字符串（str）。
Author: Lambert

你会学到：
1) 字符串创建：单引号/双引号/三引号
2) 索引/切片：s[i]、s[a:b:c]
3) 常用方法：strip/lower/replace/split/join/startswith/endswith
4) 字符串是不可变的：任何“修改”都会生成新字符串
5) 编码与解码：str <-> bytes（UTF-8）

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/05_strings_str.py
"""

from __future__ import annotations


def main() -> None:
    print("1) 创建：")
    s1 = "hello"
    s2 = 'hello'
    s3 = """multi
line"""
    print("s1 =", s1)
    print("s2 =", s2)
    print("s3 =", repr(s3))

    print("\n2) 索引/切片：")
    s = "Python"
    print("s =", s)
    print("s[0] =", s[0])
    print("s[-1] =", s[-1])
    print("s[1:4] =", s[1:4])
    print("s[:2] =", s[:2])
    print("s[::2] =", s[::2])

    print("\n3) 常用方法：")
    raw = "  Alice,BOB,Charlie  "
    cleaned = raw.strip()
    print("raw     =", repr(raw))
    print("strip() =", repr(cleaned))
    print("lower() =", cleaned.lower())
    parts = [p.strip() for p in cleaned.split(",")]
    print("split ->", parts)
    print("join  ->", " | ".join(parts))
    print("startswith('Alice') ->", cleaned.startswith("Alice"))
    print("endswith('  ') ->", raw.endswith("  "))
    print("replace ->", cleaned.replace("BOB", "Bob"))

    print("\n4) 不可变性：")
    t = "hi"
    print("before:", t, "id=", hex(id(t)))
    t2 = t + "!"
    print("after :", t2, "id=", hex(id(t2)))
    print("t 仍然是：", t)

    print("\n5) 编码/解码（UTF-8）：")
    text = "你好 Python"
    data = text.encode("utf-8")
    back = data.decode("utf-8")
    print("text =", text)
    print("data(bytes) =", data)
    print("back =", back)
    print("bytes.hex =", data.hex())


if __name__ == "__main__":
    main()
