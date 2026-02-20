#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：渲染对齐文本表格（按列宽自动对齐）
Author: Lambert

题目：
实现 `render_table(rows, columns)`，要求：
1) `rows` 是 `list[dict]`，`columns` 是列名列表
2) 表格第一行是 header，第二行是分隔线（---+--- 形式）
3) 每列宽度按“列名/内容”的最大长度自动计算，内容左对齐

参考答案：
- 本文件函数实现即参考答案；`main()` 会打印表格并做最小自测。

运行：
    python3 01_Basics/08_Exercises/04_Formatting/03_render_table.py
"""

from typing import Any


def render_table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    widths: dict[str, int] = {col: len(col) for col in columns}
    for row in rows:
        for col in columns:
            widths[col] = max(widths[col], len(str(row.get(col, ""))))

    def render_row(values: list[str]) -> str:
        parts = [f"{v:<{widths[c]}}" for v, c in zip(values, columns, strict=True)]
        return " | ".join(parts)

    header = render_row(columns)
    sep = "-+-".join("-" * widths[c] for c in columns)
    body = [render_row([str(r.get(c, "")) for c in columns]) for r in rows]
    return "\n".join([header, sep, *body])


def check(label: str, ok: bool) -> None:
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}")


def main() -> None:
    rows = [{"name": "Alice", "score": 98}, {"name": "Bob", "score": 7}]
    table = render_table(rows, columns=["name", "score"])
    print(table)
    check("has_header", table.splitlines()[0].startswith("name"))
    check("has_separator", "-+-" in table.splitlines()[1])


if __name__ == "__main__":
    main()
