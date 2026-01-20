#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ 异常处理（Exception Handling）相关示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_exception_handling_basics.py", "异常是什么：traceback、能/不能 catch 的区别"),
    ("03_common_errors.py", "常见错误演示：NameError/TypeError/ValueError/..."),
    ("04_all_builtin_exceptions.py", "内置异常总览：列出 builtins 中所有异常类与层级"),
    ("05_try_statement_patterns.py", "try 语句：except/else/finally、多分支、except*（3.11+）"),
    ("06_raise_keyword_patterns.py", "raise 关键字：from/from None/re-raise/自定义异常"),
    ("07_logging_debugging.py", "代码调试（日志）：logging 分级与 logger.exception"),
    ("08_simple_calculator.py", "简单计算器：解析表达式 + 异常处理（可选 REPL）"),
    ("09_chapter_summary.py", "本章总结：关键规则 + 常见误区清单"),
    ("Exercises/01_overview.py", "练习题索引（每题一个文件）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("示例文件清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()

