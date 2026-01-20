#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：打印到文件/缓冲区（仍然是一行输出多个内容）

你会学到：
1) `file=` 参数：输出到任意“类文件对象”
2) 用 `StringIO` 捕获 print 的输出（很常见：测试、拼日志）
3) `sys.stderr`：把信息输出到错误流（区分正常输出/错误输出）

运行：
    python3 01_Basics/03_Printing/10_print_to_file_and_capture.py
"""

from io import StringIO
import sys


def main() -> None:
    buf = StringIO()

    print("name=", "Alice", "age=", 20, file=buf, sep="")
    print("score=", 98.5, file=buf, sep="")

    captured = buf.getvalue()
    print("1) 捕获到的内容（把换行显示成 \\n 方便观察）：")
    print(captured.replace("\n", "\\n"))

    print("\n2) 打印到 stderr（一行多个字段）：", file=sys.stderr)
    print("level=ERROR", "msg=Something happened", sep=" ", file=sys.stderr)


if __name__ == "__main__":
    main()

