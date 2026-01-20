#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 08：小项目——记账 CSV 报表

输入格式（每行一条记录；允许空行与 # 注释行）：
    YYYY-MM-DD,category,amount,note

题目：
1) 用 `csv.reader` 解析输入（正确处理引号/逗号），跳过空行与 `# ...` 注释行
2) 用 `Decimal` 表示金额（避免浮点误差），金额非法时抛出清晰错误
3) 按 `category` 分组求和，并按金额从高到低排序输出
4) 同时输出两种结果：
   - 对齐的纯文本报表（列：category/amount）
   - 一行 JSON 汇总（`sort_keys=True`，便于 diff）
5) 支持两种输入来源：
   - stdin 管道输入
   - 交互终端下用内置 sample 数据演示

参考答案：
- 本文件即为参考实现；直接运行会打印报表与 JSON。

运行：
    python3 01_Basics/08_Exercises/08_mini_project_expense_report.py

也支持从 stdin 读取（例如）：
    cat expenses.csv | python3 01_Basics/08_Exercises/08_mini_project_expense_report.py
"""

from __future__ import annotations

import csv
import json
import sys
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class Expense:
    date: str
    category: str
    amount: Decimal
    note: str


def parse_decimal(text: str) -> Decimal:
    try:
        return Decimal(text.strip())
    except (InvalidOperation, ValueError) as e:
        raise ValueError(f"invalid amount: {text!r}") from e


def parse_expenses(lines: list[str]) -> list[Expense]:
    cleaned: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        if line.lstrip().startswith("#"):
            continue
        cleaned.append(line)

    reader = csv.reader(cleaned)
    out: list[Expense] = []
    for row in reader:
        if len(row) != 4:
            raise ValueError(f"bad row (need 4 columns): {row!r}")
        date, category, amount, note = row
        out.append(Expense(date=date.strip(), category=category.strip(), amount=parse_decimal(amount), note=note.strip()))
    return out


def summarize_by_category(items: list[Expense]) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for it in items:
        totals[it.category] = totals.get(it.category, Decimal("0")) + it.amount
    return totals


def render_report(totals: dict[str, Decimal]) -> str:
    rows = sorted(totals.items(), key=lambda kv: (-kv[1], kv[0]))
    header_cat = "category"
    header_amt = "amount"
    w_cat = max([len(header_cat), *(len(k) for k, _ in rows)], default=len(header_cat))
    w_amt = max([len(header_amt), *(len(f"{v:.2f}") for _, v in rows)], default=len(header_amt))

    lines = [f"{header_cat:<{w_cat}} | {header_amt:>{w_amt}}", f"{'-' * w_cat}-+-{'-' * w_amt}"]
    for cat, amt in rows:
        lines.append(f"{cat:<{w_cat}} | {amt:>{w_amt}.2f}")
    return "\n".join(lines)


def load_input_lines() -> list[str]:
    if not sys.stdin.isatty():
        return sys.stdin.read().splitlines()

    return [
        "# sample data (you can pipe your own file via stdin)\n",
        '2025-12-15,food,12.50,"lunch"\n',
        '2025-12-15,transport,3.20,"bus"\n',
        '2025-12-16,food,7.80,"coffee"\n',
        " \n",
        "# end\n",
    ]


def main() -> None:
    lines = load_input_lines()
    expenses = parse_expenses(lines)
    totals = summarize_by_category(expenses)

    print("=== Expense Report ===")
    print(render_report(totals))
    print()

    summary = {
        "total": f"{sum(totals.values(), Decimal('0')):.2f}",
        "by_category": {k: f"{v:.2f}" for k, v in sorted(totals.items())},
    }
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
