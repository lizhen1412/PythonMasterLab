#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 06：raise 关键字的各种用法（raise / raise from / raise from None / re-raise）
Author: Lambert

你会学到：
1) 主动抛错：raise ValueError(...)
2) 异常链：raise NewError(...) from exc（更清晰地表达“上游错误导致下游失败”）
3) 抑制上下文：raise ... from None（隐藏上游 traceback，让报错更聚焦）
4) 重新抛出：raise（保留原 traceback）
5) 自定义异常：让错误语义更贴近业务

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/06_raise_keyword_patterns.py
"""

from __future__ import annotations


class CalculationError(Exception):
    """计算相关错误（示例：自定义异常）。"""


def parse_number(text: str) -> float:
    try:
        return float(text)
    except ValueError as exc:
        raise ValueError(f"不是合法数字: {text!r}") from exc


def parse_number_suppress_context(text: str) -> float:
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"不是合法数字: {text!r}") from None


def demo_raise_and_from() -> None:
    print("\n1) raise + from（异常链）")
    try:
        parse_number("x")
    except ValueError as exc:
        print("caught:", type(exc).__name__, exc)


def demo_from_none() -> None:
    print("\n2) raise ... from None（抑制上下文）")
    try:
        parse_number_suppress_context("x")
    except ValueError as exc:
        print("caught:", type(exc).__name__, exc)


def demo_reraise() -> None:
    print("\n3) re-raise：保留原 traceback")
    try:
        try:
            int("x")
        except ValueError:
            print("inner caught -> re-raise")
            raise
    except ValueError as exc:
        print("outer caught:", type(exc).__name__, exc)


def demo_custom_exception() -> None:
    print("\n4) 自定义异常：表达业务语义")
    try:
        raise CalculationError("计算失败：不支持的输入组合")
    except CalculationError as exc:
        print("caught:", type(exc).__name__, exc)


def demo_not_implemented() -> None:
    print("\n5) NotImplementedError：占位（提示还没实现）")
    try:
        raise NotImplementedError("TODO: implement this function")
    except NotImplementedError as exc:
        print("caught:", type(exc).__name__, exc)


def main() -> None:
    demo_raise_and_from()
    demo_from_none()
    demo_reraise()
    demo_custom_exception()
    demo_not_implemented()


if __name__ == "__main__":
    main()
