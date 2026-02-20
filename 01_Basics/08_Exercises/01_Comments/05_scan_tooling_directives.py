#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 05：扫描常见工具指令注释（tooling directives）
Author: Lambert

题目：
实现 `extract_tooling_directives(source: str) -> dict[str, int]`，要求：
1) 用 tokenize 提取所有 `# ...` 注释
2) 识别并统计常见指令（大小写不敏感），例如：
   - `# noqa` / `# noqa: ...`
   - `# fmt: off` / `# fmt: on`
   - `# pragma: no cover`
   - `# type: ignore`

参考答案：
- 本文件中函数实现即为参考答案；`main()` 里带自测输出（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/01_Comments/05_scan_tooling_directives.py
"""

import io
import tokenize


def extract_tooling_directives(source: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type != tokenize.COMMENT:
            continue
        text = tok.string.lstrip("#").strip().lower()
        if not text:
            continue

        if text.startswith("noqa"):
            counts["noqa"] = counts.get("noqa", 0) + 1
            continue

        if text.startswith("fmt:"):
            value = text.split(":", 1)[1].strip()
            if value in {"off", "on"}:
                key = f"fmt:{value}"
                counts[key] = counts.get(key, 0) + 1
            continue

        if text.startswith("pragma:"):
            value = text.split(":", 1)[1].strip()
            key = f"pragma:{value}"
            counts[key] = counts.get(key, 0) + 1
            continue

        if text.startswith("type: ignore"):
            counts["type:ignore"] = counts.get("type:ignore", 0) + 1

    return counts


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    source = """x = 1  # noqa: F401
# fmt: off
y=2
# fmt: on
def f():  # pragma: no cover
    pass
z = 3  # type: ignore
"""
    directives = extract_tooling_directives(source)
    check("noqa", directives.get("noqa"), 1)
    check("fmt_off", directives.get("fmt:off"), 1)
    check("fmt_on", directives.get("fmt:on"), 1)
    check("pragma_no_cover", directives.get("pragma:no cover"), 1)
    check("type_ignore", directives.get("type:ignore"), 1)


if __name__ == "__main__":
    main()
