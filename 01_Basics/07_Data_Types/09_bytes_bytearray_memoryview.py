#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：二进制数据（bytes / bytearray / memoryview）。

你会学到：
1) bytes：不可变字节序列；常用于网络/文件/编码结果
2) bytearray：可变字节序列；可原地修改
3) memoryview：对二进制数据的“零拷贝视图”，切片不复制底层数据
4) str <-> bytes：encode/decode（最常见 UTF-8）

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/09_bytes_bytearray_memoryview.py
"""

from __future__ import annotations


def main() -> None:
    print("1) str <-> bytes：")
    text = "hello 你好"
    data = text.encode("utf-8")
    back = data.decode("utf-8")
    print("text =", text)
    print("data =", data)
    print("back =", back)

    print("\n2) bytes：索引是 int，切片还是 bytes：")
    b = b"ABC"
    print("b =", b)
    print("b[0] =", b[0])
    print("b[1:] =", b[1:])

    print("\n3) bytearray：可变：")
    ba = bytearray(b"hello")
    print("before ba =", ba)
    ba[0] = ord("H")
    print("after  ba =", ba)
    print("ba.decode ->", ba.decode("utf-8"))

    print("\n4) memoryview：零拷贝视图（对 bytearray 修改会反映到原始数据）：")
    mv = memoryview(ba)
    print("mv[:3].tobytes() ->", mv[:3].tobytes())
    mv[1] = ord("A")
    print("after mv[1]='A': ba ->", ba, "text ->", ba.decode("utf-8"))


if __name__ == "__main__":
    main()

