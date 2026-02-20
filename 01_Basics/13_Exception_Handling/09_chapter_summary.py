#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 09：异常处理——本章总结
Author: Lambert

运行（在仓库根目录执行）：
    python3 01_Basics/13_Exception_Handling/09_chapter_summary.py
"""

from __future__ import annotations


SUMMARY: list[str] = [
    "异常是运行时问题；traceback 最后一行给出异常类型与消息，配合栈帧定位根因",
    "常见异常：NameError/TypeError/ValueError/IndexError/KeyError/AttributeError/ZeroDivisionError",
    "业务代码通常 catch Exception；避免无脑 except:（会吞掉 KeyboardInterrupt/SystemExit）",
    "try 语句：try/except、多分支 except、except(A,B)、else（成功路径）、finally（一定执行）",
    "raise：主动抛错、re-raise（raise）、异常链（raise ... from exc）、抑制上下文（from None）",
    "logging：用分级日志做调试；except 中用 logger.exception 输出带 traceback 的日志",
    "把错误处理写成“可预测的行为”：给出清晰提示/返回默认值/重试/记录日志/清理资源",
]


def main() -> None:
    print("本章总结（Exception Handling）：")
    for i, line in enumerate(SUMMARY, start=1):
        print(f"{i}. {line}")
    print("\n下一步：运行练习题索引 -> python3 01_Basics/13_Exception_Handling/Exercises/01_overview.py")


if __name__ == "__main__":
    main()
