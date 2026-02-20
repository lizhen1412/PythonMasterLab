#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：bytes/bytearray/memoryview（原地修改缓冲区）
Author: Lambert

题目：
实现 `patch_bytearray(data)`，要求：
- 接收 `bytearray`
- 用 `memoryview` 修改其中一段切片（原地修改）
- 返回修改后的 bytes 结果

参考答案：
- 本文件函数实现即参考答案；`main()` 带最小自测（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/07_Data_Types/05_bytes_memoryview_patch.py
"""


def patch_bytearray(data: bytearray) -> bytes:
    view = memoryview(data)
    view[1:3] = b"OK"
    return bytes(view)


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    raw = bytearray(b"X__Z")
    patched = patch_bytearray(raw)
    check("raw", bytes(raw), b"XOKZ")
    check("patched", patched, b"XOKZ")


if __name__ == "__main__":
    main()
