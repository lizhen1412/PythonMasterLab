#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 52：字符串方法完整版。

运行：
    python3 02_Frameworks/01_Pandas/52_string_methods_complete.py

知识点：
- 大小写转换：lower/upper/capitalize/title/swaptopcase/casefold
- 空白处理：strip/lstrip/rstrip/strip
- 查找替换：find/rfind/index/rindex/contains
- 分割连接：split/rsplit/partition/rpartition
- 匹配验证：startswith/endswith/match/fullmatch
- 提取：extract/extract_all/get_dummies
- 格式化：pad/center/ljust/rjust/zfill
- 其他：len/repeat/replace/cat/join
"""

from __future__ import annotations

import pandas as pd


def main() -> None:
    # 创建示例 Series
    s = pd.Series(
        ["  Hello World  ", "Python", "PANDAS", "data-science", None, "123"],
        index=["a", "b", "c", "d", "e", "f"],
    )

    print("=" * 70)
    print("原始 Series")
    print("=" * 70)
    print(s)

    print("\n" + "=" * 70)
    print("1. 大小写转换")
    print("=" * 70)

    print("str.lower() ->")
    print(s.str.lower())

    print("\nstr.upper() ->")
    print(s.str.upper())

    print("\nstr.capitalize() ->")
    print(s.str.capitalize())

    print("\nstr.title() ->")
    print(s.str.title())

    print("\nstr.swapcase() ->")
    print(s.str.swapcase())

    print("\nstr.casefold() ->")
    print(s.str.casefold())

    print("\n" + "=" * 70)
    print("2. 空白处理")
    print("=" * 70)

    s_spaces = pd.Series(["  hello  ", "\tworld\n", "  pandas  "])
    print("原始 ->")
    print(repr(s_spaces.tolist()))

    print("\nstr.strip() ->")
    print(s_spaces.str.strip())

    print("\nstr.lstrip() ->")
    print(s_spaces.str.lstrip())

    print("\nstr.rstrip() ->")
    print(s_spaces.str.rstrip())

    print("\n" + "=" * 70)
    print("3. 查找与搜索")
    print("=" * 70)

    s_search = pd.Series(["hello world", "python pandas", "data analysis"])
    print("原始 ->")
    print(s_search)

    print("\nstr.find('a') ->")
    print(s_search.str.find("a"))

    print("\nstr.rfind('a') ->")
    print(s_search.str.rfind("a"))

    print("\nstr.index('a') ->")
    print(s_search.str.index("a"))

    print("\nstr.rindex('a') ->")
    print(s_search.str.rindex("a"))

    print("\nstr.contains('a') ->")
    print(s_search.str.contains("a"))

    print("\nstr.contains('a|p') ->")
    print(s_search.str.contains("a|p", regex=True))

    print("\nstr.contains('a', case=False) ->")
    print(s_search.str.contains("a", case=False))

    print("\nstr.match('h.*') ->")
    print(s_search.str.match("h.*"))

    print("\nstr.fullmatch('hello.*') ->")
    print(s_search.str.fullmatch("hello.*"))

    print("\nstr.count('a') ->")
    print(s_search.str.count("a"))

    print("\n" + "=" * 70)
    print("4. 分割与连接")
    print("=" * 70)

    s_split = pd.Series(["a-b-c", "x-y-z", "1-2-3"])
    print("原始 ->")
    print(s_split)

    print("\nstr.split('-') ->")
    print(s_split.str.split("-"))

    print("\nstr.split('-', expand=True) ->")
    print(s_split.str.split("-", expand=True))

    print("\nstr.split('-', n=1) ->")
    print(s_split.str.split("-", n=1))

    print("\nstr.rsplit('-', n=1) ->")
    print(s_split.str.rsplit("-", n=1))

    print("\nstr.partition('-') ->")
    print(s_split.str.partition("-"))

    print("\nstr.rpartition('-') ->")
    print(s_split.str.rpartition("-"))

    # 连接
    s_join = pd.Series([["a", "b"], ["c", "d"], ["e", "f"]])
    print("\n原始列表 Series ->")
    print(s_join)

    print("\nstr.join('-') ->")
    print(s_join.str.join("-"))

    print("\nstr.cat() 连接字符串 ->")
    s_cat = pd.Series(["a", "b", "c"])
    print(s_cat.str.cat(sep="-"))
    print(s_cat.str.cat(sep=", ", na_rep="NA"))

    print("\n" + "=" * 70)
    print("5. 替换")
    print("=" * 70)

    s_replace = pd.Series(["hello world", "python programming"])
    print("原始 ->")
    print(s_replace)

    print("\nstr.replace('o', 'O') ->")
    print(s_replace.str.replace("o", "O"))

    print("\nstr.replace('o', 'O', n=1) ->")
    print(s_replace.str.replace("o", "O", n=1))

    print("\nstr.replace('o.*o', 'X', regex=True) ->")
    print(s_replace.str.replace("o.*o", "X", regex=True))

    print("\n" + "=" * 70)
    print("6. 提取")
    print("=" * 70)

    s_extract = pd.Series(["abc123", "def456", "ghi789"])
    print("原始 ->")
    print(s_extract)

    print("\nstr.extract(r'(\\w{3})(\\d{3}') ->")
    print(s_extract.str.extract(r"(\w{3})(\d{3})"))

    print("\nstr.extractall(r'\\d') ->")
    print(s_extract.str.extractall(r"\d"))

    print("\nstr.slice(0, 3) ->")
    print(s_extract.str.slice(0, 3))

    print("\nstr.slice(1, -1) ->")
    print(s_extract.str.slice(1, -1))

    print("\nstr[0:3] ->")
    print(s_extract.str[0:3])

    print("\n" + "=" * 70)
    print("7. 格式化与对齐")
    print("=" * 70)

    s_pad = pd.Series(["a", "bb", "ccc"])
    print("原始 ->")
    print(s_pad)

    print("\nstr.pad(5, side='left', fillchar='_') ->")
    print(s_pad.str.pad(5, side="left", fillchar="_"))

    print("\nstr.center(5, fillchar='_') ->")
    print(s_pad.str.center(5, fillchar="_"))

    print("\nstr.ljust(5, fillchar='_') ->")
    print(s_pad.str.ljust(5, fillchar="_"))

    print("\nstr.rjust(5, fillchar='_') ->")
    print(s_pad.str.rjust(5, fillchar="_"))

    print("\nstr.zfill(5) ->")
    print(s_pad.str.zfill(5))

    print("\n" + "=" * 70)
    print("8. 长度与重复")
    print("=" * 70)

    print("str.len() ->")
    print(s.str.len())

    print("\nstr.repeat(2) ->")
    print(s.str.repeat(2))

    print("\n" + "=" * 70)
    print("9. 前缀与后缀")
    print("=" * 70)

    s_prefix = pd.Series(["prefix_value", "prefix_test", "other_value"])
    print("原始 ->")
    print(s_prefix)

    print("\nstr.removeprefix('prefix_') ->")
    print(s_prefix.str.removeprefix("prefix_"))

    print("\nstr.removesuffix('_value') ->")
    print(s_prefix.str.removesuffix("_value"))

    print("\n" + "=" * 70)
    print("10. 编码与解码")
    print("=" * 70)

    s_encode = pd.Series(["hello", "world"])
    print("原始 ->")
    print(s_encode)

    print("\nstr.encode('utf-8') ->")
    print(s_encode.str.encode("utf-8"))

    print("\n" + "=" * 70)
    print("11. get_dummies - 独热编码")
    print("=" * 70)

    s_dummy = pd.Series(["a|b", "b|c", "a|c"])
    print("原始 ->")
    print(s_dummy)

    print("\nstr.get_dummies('|') ->")
    print(s_dummy.str.get_dummies("|"))

    print("\n" + "=" * 70)
    print("12. 验证方法")
    print("=" * 70)

    s_validate = pd.Series(["hello", "123", "Hello123", "", "   "])
    print("原始 ->")
    print(s_validate)

    print("\nstr.isalpha() ->")
    print(s_validate.str.isalpha())

    print("\nstr.isnumeric() ->")
    print(s_validate.str.isnumeric())

    print("\nstr.isdigit() ->")
    print(s_validate.str.isdigit())

    print("\nstr.isdecimal() ->")
    print(s_validate.str.isdecimal())

    print("\nstr.isalnum() ->")
    print(s_validate.str.isalnum())

    print("\nstr.isspace() ->")
    print(s_validate.str.isspace())

    print("\nstr.islower() ->")
    print(s_validate.str.islower())

    print("\nstr.isupper() ->")
    print(s_validate.str.isupper())

    print("\nstr.istitle() ->")
    print(s_validate.str.istitle())

    print("\n" + "=" * 70)
    print("13. 实际应用示例")
    print("=" * 70)

    # 示例 1: 清洗用户输入
    print("示例 1: 清洗用户输入")
    user_input = pd.Series(["  Alice@Example.com  ", "  BOB@test.com  ", "  cathy@demo.com  "])
    cleaned = user_input.str.strip().str.lower().str.replace(r".*@(.*)", r"\1", regex=True)
    print(f"原始: {user_input.tolist()}")
    print(f"提取域名: {cleaned.tolist()}")

    # 示例 2: 解析日志
    print("\n示例 2: 解析日志文件")
    logs = pd.Series(
        [
            "[2024-01-01 10:00:00] ERROR: File not found",
            "[2024-01-01 10:01:00] WARNING: Low memory",
            "[2024-01-01 10:02:00] INFO: Task completed",
        ]
    )
    log_df = logs.str.extract(r"\[([^\]]+)\]\s+(\w+):\s+(.*)")
    log_df.columns = ["timestamp", "level", "message"]
    print(log_df)

    # 示例 3: 提取电话号码
    print("\n示例 3: 提取和格式化电话号码")
    phones = pd.Series(["(123) 456-7890", "555-123-4567", "123.456.7890"])
    # 移除所有非数字字符
    cleaned_phones = phones.str.replace(r"\D", "", regex=True)
    # 重新格式化
    formatted = (
        cleaned_phones.str.extract(r"(\d{3})(\d{3})(\d{4})")
        .apply(lambda x: "(" + x[0] + ") " + x[1] + "-" + x[2], axis=1)
        .squeeze()
    )
    print(f"原始: {phones.tolist()}")
    print(f"格式化: {formatted.tolist()}")

    # 示例 4: 检查电子邮件格式
    print("\n示例 4: 验证电子邮件格式")
    emails = pd.Series(["user@example.com", "invalid.email", "@missing.com", "valid@test.co"])
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    print(f"原始: {emails.tolist()}")
    print(f"是否有效: {emails.str.match(email_pattern, na=False).tolist()}")

    # 示例 5: 文本分类
    print("\n示例 5: 根据关键词分类文本")
    texts = pd.Series(
        ["The price is $100", "Discount 50% off", "Free shipping", "Sale ends tomorrow", "Buy now"]
    )
    def classify_text(text):
        if pd.isna(text):
            return "unknown"
        text_lower = text.lower()
        if any(word in text_lower for word in ["price", "$", "cost"]):
            return "price_info"
        elif any(word in text_lower for word in ["discount", "off", "sale"]):
            return "promotion"
        elif any(word in text_lower for word in ["free", "shipping"]):
            return "shipping"
        else:
            return "other"

    categories = texts.apply(classify_text)
    print(f"文本: {texts.tolist()}")
    print(f"分类: {categories.tolist()}")

    print("\n" + "=" * 70)
    print("14. 常见陷阱")
    print("=" * 70)

    print("""
常见陷阱：
1. str 方法会跳过 NaN 值，不会报错
2. 某些方法（如 split）返回列表，可能需要 expand=True
3. regex=True 是默认的，注意转义特殊字符
4. 大小写方法可能不适用于所有语言（考虑 casefold）
5. strip 默认删除空白，不只是空格
6. replace 的 n 参数在 regex=True 时可能不按预期工作
""")

    print("\nNaN 处理示例:")
    s_nan = pd.Series(["hello", None, "world"])
    print(f"原始: {s_nan.tolist()}")
    print(f"str.upper(): {s_nan.str.upper().tolist()}")
    print(f"str.contains('e', na=False): {s_nan.str.contains('e', na=False).tolist()}")


if __name__ == "__main__":
    main()
