# Python 3.11+ 格式化输出（Formatting）学习笔记

本章是一组“可运行的小脚本”，目标是把 **Python 输出格式化的所有常见方式** 一次讲清楚，并配套学习案例：f-string、格式化规格（对齐/宽度/精度/分组/进制）、`format()`/`__format__`、`str.format/format_map`、旧式 `%`、`string.Template`、`datetime` 格式化、结构化输出（pprint/JSON）、文本排版（textwrap）、以及 logging 的工程化格式化方式。

---

## 1) 怎么运行（小白版）

假设你当前在仓库根目录（能看到 `01_Basics/` 那层）：

- 先看索引：`python3 01_Basics/04_Formatting/01_overview.py`
- 运行某个示例：`python3 01_Basics/04_Formatting/03_fstrings_basics.py`

Windows 上如果没有 `python3`，可以试：

- `python 01_Basics/04_Formatting/03_fstrings_basics.py`
- 或 `py -3.11 01_Basics/04_Formatting/03_fstrings_basics.py`

---

## 2) 术语小抄（先把概念对齐）

- **格式化（formatting）**：把变量/对象变成“你想要的字符串形式”。（格式化 ≠ 打印；打印只是把字符串输出到某个地方）
- **format spec（格式化规格）**：写在 `:` 后面的那串规则，例如 `{pi:.2f}` 里的 `.2f`。
- **f-string**：`f"..."`，推荐的现代格式化方式。
- **`str` vs `repr`**：`str()`更面向用户；`repr()`更面向调试/日志（尽量不丢信息）。

---

## 3) 文件总览（先知道每个文件干什么）

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出所有示例与主题 |
| 02 | [`02_str_repr_ascii.py`](02_str_repr_ascii.py) | str/repr/ascii：人读 vs 调试读 |
| 03 | [`03_fstrings_basics.py`](03_fstrings_basics.py) | f-string：表达式、`{var=}`、`!r/!s/!a`、转义 |
| 04 | [`04_format_spec_integers.py`](04_format_spec_integers.py) | 格式化规格：整数（进制/对齐/填充/分组/符号） |
| 05 | [`05_format_spec_floats_and_decimal.py`](05_format_spec_floats_and_decimal.py) | 格式化规格：浮点/Decimal（精度/科学计数/百分比） |
| 06 | [`06_format_spec_strings.py`](06_format_spec_strings.py) | 格式化规格：字符串（宽度/对齐/截断） |
| 07 | [`07_format_and___format__.py`](07_format_and___format__.py) | `format()` 与 `__format__`：自定义对象格式化 |
| 08 | [`08_str_format_and_format_map.py`](08_str_format_and_format_map.py) | `str.format/format_map`：位置/命名/属性/索引字段 |
| 09 | [`09_percent_formatting.py`](09_percent_formatting.py) | 旧式 `%`：tuple/dict 两种风格（为了看懂旧代码） |
| 10 | [`10_string_template.py`](10_string_template.py) | `string.Template`：$name 替换与 safe_substitute |
| 11 | [`11_datetime_formatting.py`](11_datetime_formatting.py) | `datetime`：strftime、`f"{dt:%Y-%m-%d}"`、isoformat |
| 12 | [`12_pprint_json_reprlib.py`](12_pprint_json_reprlib.py) | 结构化输出：pprint/json/reprlib |
| 13 | [`13_textwrap_and_layout.py`](13_textwrap_and_layout.py) | 文本排版：textwrap 换行/缩进 + 列布局 |
| 14 | [`14_logging_formatting.py`](14_logging_formatting.py) | logging：Formatter 与推荐写法（参数化日志） |
| 15 | [`15_common_pitfalls_and_escaping.py`](15_common_pitfalls_and_escaping.py) | 常见坑：转义/类型不匹配/格式码错误等 |

---

## 4) 你要掌握的知识点（Checklist）

- 什么时候用 `str` / `repr` / `ascii`
- f-string 的 `{var=}`、`!r/!s/!a`、以及大括号转义
- format spec：整数/浮点/字符串的常用格式（对齐、宽度、精度、分组、进制）
- `format(value, spec)` / `__format__` 的工作机制（自定义对象如何格式化）
- `str.format` / `format_map` 的常见字段写法（位置、命名、属性、索引）
- `%` 格式化：能看懂 tuple/dict 两种写法
- `string.Template`：适合“受限模板/用户模板”的场景
- `datetime` 的常见输出（strftime / isoformat / f-string 格式）
- 结构化输出：pprint（人读）/ JSON（机器读）/ reprlib（防刷屏）
- logging：为什么工程里更推荐 logger 而不是满屏 print
- 常见坑：忘写 f、转义错误、格式码不匹配类型

---

## 5) 推荐学习顺序

1) 先把“输出给谁看”搞清楚：`02_str_repr_ascii.py`  
2) 重点掌握 f-string + format spec：`03`～`06`  
3) 再掌握“底层机制”和旧写法：`07`～`10`  
4) 最后补齐工程场景：`11`～`14`，以及 `15` 的坑点复盘  
