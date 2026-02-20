#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
练习 02：识别 shebang 与 encoding 声明（coding cookie）
Author: Lambert

题目：
1) 实现 `detect_shebang(lines: list[str]) -> str | None`
   - 仅当第一行以 `#!` 开头时返回该行（去掉末尾换行）
2) 实现 `detect_coding_cookie(lines: list[str]) -> str | None`
   - 仅在前两行里查找 encoding 声明，例如：
     - `# -*- coding: utf-8 -*-`
     - `# coding: utf-8`

参考答案：
- 本文件中上述函数的实现即为参考答案；`main()` 里带自测输出（[OK]/[FAIL]）。

运行：
    python3 01_Basics/08_Exercises/01_Comments/02_shebang_and_coding_cookie.py
"""

import re


def detect_shebang(lines: list[str]) -> str | None:
    if not lines:
        return None
    first = lines[0].rstrip("\n")
    return first if first.startswith("#!") else None


_CODING_COOKIE_RE = re.compile(r"^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)", re.IGNORECASE)


def detect_coding_cookie(lines: list[str]) -> str | None:
    for line in lines[:2]:
        m = _CODING_COOKIE_RE.match(line)
        if m:
            return m.group(1)
    return None


def check(label: str, got: object, expected: object) -> None:
    ok = got == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {label}: got={got!r} expected={expected!r}")


def main() -> None:
    source = "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\nprint('hi')\n"
    lines = source.splitlines(keepends=True)
    check("shebang", detect_shebang(lines), "#!/usr/bin/env python3")
    check("coding_cookie", detect_coding_cookie(lines), "utf-8")

    source2 = "print('no header')\n"
    lines2 = source2.splitlines(keepends=True)
    check("shebang_none", detect_shebang(lines2), None)
    check("coding_cookie_none", detect_coding_cookie(lines2), None)


if __name__ == "__main__":
    main()
