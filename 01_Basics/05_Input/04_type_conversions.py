#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 04：类型转换（把 input() 得到的 str 变成你需要的类型）。

关键事实：
- `input()` 永远返回 str；想要 int/float/bool/Decimal，必须自己转换。

你会学到：
1) int / float / Decimal 的常见转换
2) 处理转换失败：捕获 ValueError（不要让程序直接崩）
3) 解析 bool：需要自己定义规则（比如 y/n、true/false）

运行（在仓库根目录执行）：
    python3 01_Basics/05_Input/04_type_conversions.py
"""

from __future__ import annotations

from decimal import Decimal


TRUE_SET = {"1", "true", "t", "yes", "y", "on"}
FALSE_SET = {"0", "false", "f", "no", "n", "off"}


def parse_bool(text: str) -> bool:
    normalized = text.strip().lower()
    if normalized in TRUE_SET:
        return True
    if normalized in FALSE_SET:
        return False
    raise ValueError(f"cannot parse bool from {text!r}")


def main() -> None:
    try:
        raw_age = input("请输入年龄（整数；直接回车使用 18）：").strip()
        age = int(raw_age) if raw_age else 18
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：age 使用默认 18")
        age = 18
    except ValueError as exc:
        print("年龄不是合法整数：", exc)
        age = 18

    try:
        raw_score = input("请输入分数（浮点数；例如 98.5；直接回车使用 0）：").strip()
        score = float(raw_score) if raw_score else 0.0
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：score 使用默认 0.0")
        score = 0.0
    except ValueError as exc:
        print("分数不是合法浮点数：", exc)
        score = 0.0

    try:
        raw_price = input("请输入价格（Decimal；例如 19.99；直接回车使用 0）：").strip()
        price = Decimal(raw_price) if raw_price else Decimal("0")
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：price 使用默认 0")
        price = Decimal("0")
    except Exception as exc:
        # Decimal 转换失败常见异常是 decimal.InvalidOperation（这里用 Exception 统一演示）
        print("价格不是合法 Decimal：", exc)
        price = Decimal("0")

    try:
        raw_ok = input("是否继续？[y/n]（例如 y、n、true、false）：").strip()
        ok = parse_bool(raw_ok)
    except (EOFError, KeyboardInterrupt):
        print("\n未输入：ok 默认 False")
        ok = False
    except ValueError as exc:
        print("无法解析布尔值：", exc)
        ok = False

    print("\n解析结果：")
    print(f"age={age} (type={type(age).__name__})")
    print(f"score={score} (type={type(score).__name__})")
    print(f"price={price} (type={type(price).__name__})")
    print(f"ok={ok} (type={type(ok).__name__})")


if __name__ == "__main__":
    main()

