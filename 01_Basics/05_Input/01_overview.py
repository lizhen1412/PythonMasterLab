#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 01：Python 3.11+ input() 相关示例索引。

运行方式（在仓库根目录执行）：
    python3 01_Basics/05_Input/01_overview.py
"""

from __future__ import annotations

from pathlib import Path


TOPICS: list[tuple[str, str]] = [
    ("02_input_basics.py", "input() 基础：返回值、提示语、空白与换行"),
    ("03_strip_and_default.py", "strip 与默认值：处理空输入/空白输入"),
    ("04_type_conversions.py", "类型转换：int/float/Decimal/bool（含安全处理）"),
    ("05_multiple_values_split.py", "一行输入多个值：split/unpack/map/shlex.split"),
    ("06_validation_loops.py", "校验与重试：范围检查、选择题、yes/no"),
    ("07_multiline_until_sentinel.py", "多行输入：直到哨兵（END）或空行结束"),
    ("08_eof_and_interrupt.py", "EOFError / KeyboardInterrupt：优雅退出"),
    ("09_getpass_secret_input.py", "密码/密钥输入：getpass（不回显）"),
    ("10_sys_stdin_readline_and_pipe.py", "sys.stdin：readline/read 到 EOF；配合管道/重定向"),
    ("11_testable_input_functions.py", "可测试的输入代码：注入 input_func + StringIO"),
    ("12_structured_input_parsing.py", "结构化输入：json.loads 与 ast.literal_eval（安全解析）"),
    ("13_cli_args_and_argparse.py", "命令行参数：sys.argv 与 argparse"),
    ("14_environment_variables.py", "环境变量输入：os.environ/os.getenv"),
    ("15_stdin_binary_and_encoding.py", "二进制 stdin：sys.stdin.buffer 与解码"),
    ("16_fileinput_multiple_sources.py", "多来源输入：fileinput 统一处理文件与 stdin"),
    ("17_readline_history_and_completion.py", "readline：历史记录与补全（平台可选）"),
    ("18_nonblocking_and_timeout_input.py", "非阻塞/超时输入：select 等待 stdin"),
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
