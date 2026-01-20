#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 12：str 方法全覆盖（Python 3.11+）。

你会学到：
1) 清理与切分：strip/split/partition/expandtabs 等
2) 查找与计数：find/index/count/startswith/endswith
3) 替换与翻译：replace/translate/maketrans
4) 大小写与样式：lower/upper/title/swapcase/casefold
5) 对齐与填充：center/ljust/rjust/zfill
6) 判断类 is*：isalpha/isdigit/isnumeric/... 等
7) 拼接/格式化/编码：join/format/format_map/encode

运行（在仓库根目录执行）：
    python3 01_Basics/07_Data_Types/12_str_methods_reference.py
"""

from __future__ import annotations


def show(title: str) -> None:
    print(f"\n{title}\n" + "-" * len(title))


def demo(label: str, value: object) -> None:
    print(f"{label:<30} -> {value!r}")


def main() -> None:
    show("1) 清理与切分")
    raw = "  hello\tworld  \n"
    demo("strip()", raw.strip())
    demo("lstrip()", raw.lstrip())
    demo("rstrip()", raw.rstrip())
    demo("removeprefix('  ')", raw.removeprefix("  "))
    demo("removesuffix('\\n')", raw.removesuffix("\n"))
    demo("expandtabs(4)", "a\tb\tc".expandtabs(4))

    data = "a,b,c,d"
    demo("split(',')", data.split(","))
    demo("split(',', 2)", data.split(",", 2))
    demo("rsplit(',', 2)", data.rsplit(",", 2))

    lines = "a\nb\r\nc"
    demo("splitlines()", lines.splitlines())
    demo("splitlines(keepends=True)", lines.splitlines(keepends=True))

    chain = "a-b-c"
    demo("partition('-')", chain.partition("-"))
    demo("rpartition('-')", chain.rpartition("-"))

    show("2) 查找与计数")
    s = "banana"
    demo("count('na')", s.count("na"))
    demo("find('na')", s.find("na"))
    demo("find('na', 3)", s.find("na", 3))
    demo("rfind('na')", s.rfind("na"))
    demo("index('na')", s.index("na"))
    demo("rindex('na')", s.rindex("na"))
    demo("find('xy')", s.find("xy"))
    try:
        s.index("xy")
    except ValueError as exc:
        print("index('xy') -> ValueError:", exc)
    demo("startswith('ba')", s.startswith("ba"))
    demo("startswith(('ba','ha'))", s.startswith(("ba", "ha")))
    demo("endswith('na')", s.endswith("na"))

    show("3) 替换与翻译")
    demo("replace('na','NA')", s.replace("na", "NA"))
    demo("replace('na','NA', 1)", s.replace("na", "NA", 1))

    leet_table = str.maketrans({"a": "4", "e": "3", "i": "1", "o": "0"})
    demo("translate(leet)", "aeio".translate(leet_table))
    swap_table = str.maketrans("abc", "123")
    demo("translate('abc'->'123')", "cab".translate(swap_table))
    delete_vowels = str.maketrans("", "", "aeiou")
    demo("translate(delete vowels)", "banana".translate(delete_vowels))

    show("4) 大小写与样式")
    text = "hello WORLD"
    demo("lower()", text.lower())
    demo("upper()", text.upper())
    demo("capitalize()", text.capitalize())
    demo("title()", "hello world".title())
    demo("swapcase()", "PyThOn".swapcase())
    demo("casefold()", "Straße".casefold())

    show("5) 对齐与填充")
    demo("center(10, '-')", "cat".center(10, "-"))
    demo("ljust(10, '.')", "cat".ljust(10, "."))
    demo("rjust(10, '.')", "cat".rjust(10, "."))
    demo("zfill(6)", "42".zfill(6))
    demo("zfill(6) on -42", "-42".zfill(6))

    show("6) 判断类 is*")
    basic_samples = ["abc", "abc123", "café", "变量", "123", " \t", "hi\n"]
    for sample in basic_samples:
        print(
            f"{sample!r:<10} "
            f"isalpha={sample.isalpha():<5} "
            f"isalnum={sample.isalnum():<5} "
            f"isascii={sample.isascii():<5} "
            f"isprintable={sample.isprintable():<5} "
            f"isspace={sample.isspace():<5}"
        )

    id_samples = ["var_1", "1var", "变量"]
    for sample in id_samples:
        print(f"isidentifier({sample!r}) -> {sample.isidentifier()}")

    numeric_samples = ["123", "①", "Ⅷ", "四"]
    for sample in numeric_samples:
        print(
            f"{sample!r:<4} "
            f"isdecimal={sample.isdecimal():<5} "
            f"isdigit={sample.isdigit():<5} "
            f"isnumeric={sample.isnumeric():<5}"
        )

    case_samples = ["abc", "ABC", "Hello World", "hello world"]
    for sample in case_samples:
        print(
            f"{sample!r:<12} "
            f"islower={sample.islower():<5} "
            f"isupper={sample.isupper():<5} "
            f"istitle={sample.istitle():<5}"
        )

    show("7) 拼接/格式化/编码")
    demo("join(['a','b'])", ",".join(["a", "b"]))
    template = "name={name} score={score:.1f}"
    demo("format()", template.format(name="Alice", score=98.5))
    demo("format_map()", template.format_map({"name": "Bob", "score": 7}))
    demo("encode('utf-8')", "你好".encode("utf-8"))


if __name__ == "__main__":
    main()
