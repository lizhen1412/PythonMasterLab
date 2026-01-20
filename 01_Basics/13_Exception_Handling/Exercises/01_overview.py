#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习索引：异常处理（Exception Handling）章节练习（每题一个文件）。

运行方式（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/Exercises/01_overview.py
"""

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_safe_divide.py", "安全除法：处理 0 和非法参数"),
    ("03_parse_int_strict.py", "严格解析 int：自定义错误信息 + 异常链"),
    ("04_validate_age_raise.py", "用 raise 做参数校验（ValueError/TypeError）"),
    ("05_read_first_line_try_finally.py", "try/finally 做资源清理（示例含清理临时文件）"),
    ("06_custom_exception_withdraw.py", "自定义异常：余额不足（业务语义）"),
    ("07_reraise_and_from_none.py", "re-raise 与 from None 的对比（__cause__/__context__）"),
    ("08_logging_exception_helper.py", "用 logging.exception 记录错误并返回默认值"),
    ("09_simple_calculator_core.py", "实现计算器核心函数（不使用 eval）"),
    ("10_retry_until_success.py", "失败重试：捕获异常并在最后抛出"),
    ("11_exception_group_parse_many.py", "进阶：ExceptionGroup + except*（Py 3.11+）"),
]


def main() -> None:
    here = Path(__file__).resolve().parent
    print(f"目录: {here}")
    print("练习题清单：")
    for filename, desc in TOPICS:
        marker = "OK" if (here / filename).exists() else "MISSING"
        print(f"- {marker} {filename}: {desc}")


if __name__ == "__main__":
    main()

