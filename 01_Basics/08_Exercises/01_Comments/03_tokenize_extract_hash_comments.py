#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 03：用 tokenize 提取 # 注释
Author: Lambert

题目：
实现 `extract_hash_comments(source: str) -> list[str]`，要求：
1) 返回源码中所有 `# ...` 注释 token（包含 shebang/coding cookie/行尾注释）
2) 字符串里的 `#` 不算注释（例如 `"# not a comment"`）

参考答案：
- 本文件中 `extract_hash_comments` 的实现即为参考答案；`main()` 里带自测输出（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/01_Comments/03_tokenize_extract_hash_comments.py
"""

import io
import tokenize


def extract_hash_comments(source: str) -> list[str]:
    comments: list[str] = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type == tokenize.COMMENT:
            comments.append(tok.string)
    return comments


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    source = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# top
x = "# not a comment"  # inline
"""
    comments = extract_hash_comments(source)
    check("comment_count", len(comments), 4)
    check("first_is_shebang", comments[0], "#!/usr/bin/env python3")
    check("has_inline", "# inline" in comments, True)


if __name__ == "__main__":
    main()
