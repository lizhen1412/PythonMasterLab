#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 10：string.Template（$name 风格的模板替换）。
Author: Lambert

适用场景：
- 你想要一个“更简单、更受限”的模板语法（避免 format/f-string 的表达式能力）
- 或者你要处理用户提供的模板字符串（降低出错/注入风险）

你会学到：
1) `Template("...$name...").substitute(mapping)`
2) `safe_substitute`：缺字段时不报错
3) 输出字面量 `$`：写成 `$$`

运行：
    python3 01_Basics/04_Formatting/10_string_template.py
"""

from string import Template


def main() -> None:
    tpl = Template("user=$name age=$age score=$score $$USD")
    data = {"name": "Alice", "age": 20, "score": 98.5}

    print("1) substitute：")
    print(tpl.substitute(data))

    print("\n2) safe_substitute（缺字段也能跑）：")
    partial = {"name": "Bob"}
    print(tpl.safe_substitute(partial))


if __name__ == "__main__":
    main()
