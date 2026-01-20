#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 15：二进制类型方法全覆盖（bytes / bytearray / memoryview）。

你会学到：
1) bytes/bytearray 的字符串风格方法
2) bytearray 的可变操作方法
3) memoryview 的常用属性与方法

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/15_binary_types_methods_reference.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<30} -> {value!r}")


def demo_bytes() -> None:
    show("1) bytes 方法")
    b = b"  Abc\t123\n"
    demo("capitalize()", b.capitalize())
    demo("lower()", b.lower())
    demo("upper()", b.upper())
    demo("swapcase()", b.swapcase())
    demo("title()", b"title case".title())
    demo("center(12, b'-')", b"hi".center(12, b"-"))
    demo("ljust(6, b'.')", b"hi".ljust(6, b"."))
    demo("rjust(6, b'.')", b"hi".rjust(6, b"."))
    demo("zfill(6)", b"42".zfill(6))
    demo("strip()", b.strip())
    demo("lstrip()", b.lstrip())
    demo("rstrip()", b.rstrip())
    demo("removeprefix(b'  ')", b.removeprefix(b"  "))
    demo("removesuffix(b'\\n')", b.removesuffix(b"\n"))
    demo("expandtabs(4)", b"hi\tthere".expandtabs(4))

    demo("count(b'1')", b.count(b"1"))
    demo("find(b'c')", b.find(b"c"))
    demo("rfind(b'1')", b.rfind(b"1"))
    demo("index(b'c')", b.index(b"c"))
    demo("rindex(b'1')", b.rindex(b"1"))
    demo("startswith(b'  ')", b.startswith(b"  "))
    demo("endswith(b'\\n')", b.endswith(b"\n"))

    demo("split()", b.split())
    demo("split(b'c')", b.split(b"c"))
    demo("rsplit(b'1', 1)", b.rsplit(b"1", 1))
    demo("splitlines()", b.splitlines())
    demo("partition(b'c')", b.partition(b"c"))
    demo("rpartition(b'1')", b.rpartition(b"1"))

    demo("replace(b'1', b'9')", b.replace(b"1", b"9"))
    demo("join([b'a', b'b'])", b"-".join([b"a", b"b"]))
    demo("decode('utf-8')", b"hi".decode("utf-8"))

    demo("isalnum()", b"ABC123".isalnum())
    demo("isalpha()", b"ABC".isalpha())
    demo("isascii()", b"\x7f".isascii())
    demo("isdigit()", b"123".isdigit())
    demo("islower()", b"abc".islower())
    demo("isspace()", b" \t".isspace())
    demo("istitle()", b"Hello World".istitle())
    demo("isupper()", b"ABC".isupper())

    table = bytes.maketrans(b"abc", b"123")
    demo("maketrans(b'abc', b'123')", table)
    demo("translate(table)", b"cab".translate(table))

    demo("hex()", b"ABC".hex())
    demo("fromhex('414243')", bytes.fromhex("414243"))


def demo_bytearray() -> None:
    show("2) bytearray 方法")
    ba = bytearray(b"  Abc\t123\n")
    demo("capitalize()", ba.capitalize())
    demo("lower()", ba.lower())
    demo("upper()", ba.upper())
    demo("swapcase()", ba.swapcase())
    demo("title()", bytearray(b"title case").title())
    demo("center(12, b'-')", bytearray(b"hi").center(12, b"-"))
    demo("ljust(6, b'.')", bytearray(b"hi").ljust(6, b"."))
    demo("rjust(6, b'.')", bytearray(b"hi").rjust(6, b"."))
    demo("zfill(6)", bytearray(b"42").zfill(6))
    demo("strip()", ba.strip())
    demo("lstrip()", ba.lstrip())
    demo("rstrip()", ba.rstrip())
    demo("removeprefix(b'  ')", ba.removeprefix(b"  "))
    demo("removesuffix(b'\\n')", ba.removesuffix(b"\n"))
    demo("expandtabs(4)", bytearray(b"hi\tthere").expandtabs(4))

    demo("count(b'1')", ba.count(b"1"))
    demo("find(b'c')", ba.find(b"c"))
    demo("rfind(b'1')", ba.rfind(b"1"))
    demo("index(b'c')", ba.index(b"c"))
    demo("rindex(b'1')", ba.rindex(b"1"))
    demo("startswith(b'  ')", ba.startswith(b"  "))
    demo("endswith(b'\\n')", ba.endswith(b"\n"))

    demo("split()", ba.split())
    demo("split(b'c')", ba.split(b"c"))
    demo("rsplit(b'1', 1)", ba.rsplit(b"1", 1))
    demo("splitlines()", ba.splitlines())
    demo("partition(b'c')", ba.partition(b"c"))
    demo("rpartition(b'1')", ba.rpartition(b"1"))

    demo("replace(b'1', b'9')", ba.replace(b"1", b"9"))
    demo("join([b'a', b'b'])", bytearray(b"-").join([b"a", b"b"]))
    demo("decode('utf-8')", bytearray(b"hi").decode("utf-8"))

    demo("isalnum()", bytearray(b"ABC123").isalnum())
    demo("isalpha()", bytearray(b"ABC").isalpha())
    demo("isascii()", bytearray(b"\x7f").isascii())
    demo("isdigit()", bytearray(b"123").isdigit())
    demo("islower()", bytearray(b"abc").islower())
    demo("isspace()", bytearray(b" \t").isspace())
    demo("istitle()", bytearray(b"Hello World").istitle())
    demo("isupper()", bytearray(b"ABC").isupper())

    table = bytearray.maketrans(b"abc", b"123")
    demo("maketrans(b'abc', b'123')", table)
    demo("translate(table)", bytearray(b"cab").translate(table))

    demo("hex()", bytearray(b"ABC").hex())
    demo("fromhex('414243')", bytearray.fromhex("414243"))

    mut = bytearray(b"abc")
    mut.append(100)
    demo("append(100)", mut)
    mut = bytearray(b"abc")
    mut.extend([100, 101])
    demo("extend([100,101])", mut)
    mut = bytearray(b"abc")
    mut.insert(1, 120)
    demo("insert(1,120)", mut)
    mut = bytearray(b"abc")
    popped = mut.pop()
    demo("pop()", popped)
    demo("after pop", mut)
    mut = bytearray(b"abca")
    mut.remove(97)
    demo("remove(97)", mut)
    mut = bytearray(b"abc")
    mut.reverse()
    demo("reverse()", mut)
    demo("copy()", mut.copy())
    mut.clear()
    demo("clear()", mut)


def demo_memoryview() -> None:
    show("3) memoryview 方法与属性")
    data = bytearray(b"abcd")
    mv = memoryview(data)
    demo("format", mv.format)
    demo("itemsize", mv.itemsize)
    demo("ndim", mv.ndim)
    demo("shape", mv.shape)
    demo("strides", mv.strides)
    demo("suboffsets", mv.suboffsets)
    demo("nbytes", mv.nbytes)
    demo("readonly", mv.readonly)
    demo("c_contiguous", mv.c_contiguous)
    demo("f_contiguous", mv.f_contiguous)
    demo("contiguous", mv.contiguous)
    demo("obj", type(mv.obj).__name__)
    demo("tobytes()", mv.tobytes())
    demo("tolist()", mv.tolist())
    demo("hex()", mv.hex())
    demo("cast('B')[:2].tolist()", mv.cast("B")[:2].tolist())
    ro = mv.toreadonly()
    demo("toreadonly().readonly", ro.readonly)

    mv2 = memoryview(bytearray(b"xy"))
    mv2.release()
    demo("release()", "released")


def main() -> None:
    demo_bytes()
    demo_bytearray()
    demo_memoryview()


if __name__ == "__main__":
    main()
