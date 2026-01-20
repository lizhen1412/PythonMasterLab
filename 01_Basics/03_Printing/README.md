# Python 3.11+ 一行打印多个内容（Printing）学习笔记

本目录是一组“可运行的小脚本”，专门解决一个非常常见的需求：

> **如何在一行里打印多个内容**（多个变量/多个对象/字典字段/格式化后的数值等），并让输出更清晰、更专业。

你会学到从 `print(a, b, c)` 的基础用法，到 `sep/end/flush`、`print(*items)`、`join`、f-string、格式化规格（对齐/精度/千分位/百分比）、以及常见错误的正确写法。

---

## 1) 怎么运行（小白版）

假设你当前在仓库根目录（能看到 `01_Basics/` 那层）：

- 先看索引：`python3 01_Basics/03_Printing/01_overview.py`
- 运行某个示例：`python3 01_Basics/03_Printing/02_print_multiple_objects.py`

Windows 上如果没有 `python3`，可以试：

- `python 01_Basics/03_Printing/02_print_multiple_objects.py`
- 或 `py -3.11 01_Basics/03_Printing/02_print_multiple_objects.py`

> 每个脚本末尾都有固定入口：`if __name__ == "__main__": main()`  
> 含义：文件被“直接运行”时执行 `main()`；被 `import` 时不会自动执行。

---

## 2) 术语小抄（先把概念对齐）

- **一行打印多个内容**：指输出结果在同一行里包含多个字段，例如 `name=Alice age=20 score=98.5`。
- **`print()`**：Python 内置函数，用来把内容写到输出流（默认是终端）。
- **`sep`**：多个对象之间的分隔符（默认空格 `" "`）。
- **`end`**：print 结尾追加的内容（默认换行 `"\n"`）。
- **`flush`**：是否立刻刷新缓冲（实时显示进度时常用）。
- **`str(obj)` / `repr(obj)`**：对象的两种字符串表示；`print(obj)` 默认用 `str(obj)`。

---

## 3) 文件总览（先知道每个文件干什么）

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出所有示例与主题 |
| 02 | [`02_print_multiple_objects.py`](02_print_multiple_objects.py) | print 基础：一次打印多个对象、`sep/end/flush`、str vs repr |
| 03 | [`03_unpacking_iterables.py`](03_unpacking_iterables.py) | 打印可迭代对象：`print(*items)`、dict/set 的注意点 |
| 04 | [`04_join_vs_sep.py`](04_join_vs_sep.py) | 拼接一行字符串：`join` vs `sep`（含非字符串元素） |
| 05 | [`05_fstring_and_debug.py`](05_fstring_and_debug.py) | f-string：一行输出多个变量、`{var=}`、`!r`、格式化 |
| 06 | [`06_format_spec_mini_language.py`](06_format_spec_mini_language.py) | 格式化规格：对齐/宽度/精度/千分位/百分比（打印表格行） |
| 07 | [`07_print_dicts_key_values.py`](07_print_dicts_key_values.py) | 一行打印 dict：`k=v`、一行 JSON、querystring |
| 08 | [`08_repr_str_and_custom_objects.py`](08_repr_str_and_custom_objects.py) | 对象怎么决定打印效果：实现 `__str__`/`__repr__` |
| 09 | [`09_same_line_update.py`](09_same_line_update.py) | 同一行刷新输出：进度条、`\r` 与 `flush=True` |
| 10 | [`10_print_to_file_and_capture.py`](10_print_to_file_and_capture.py) | `file=` 参数：打印到文件/缓冲区，捕获输出，stderr |
| 11 | [`11_common_mistakes.py`](11_common_mistakes.py) | 常见错误与正确写法：`+`、`join`、`sep` 类型等 |
| 12 | [`12_format_method_and_percent.py`](12_format_method_and_percent.py) | 旧格式化：`str.format` / `format_map` / `%`（为了看懂旧代码） |

---

## 4) 你要掌握的知识点（Checklist）

- `print(a, b, c)`：一次打印多个对象（默认用空格分隔）
- `sep`：控制分隔符（逗号、竖线、空字符串等）
- `end`：控制结尾（不换行/同一行拼接）
- `flush`：控制是否立刻刷新（进度输出）
- `print(items)` vs `print(*items)`：打印容器 vs 打印元素
- `join`：拼出“一行字符串”（写日志/写文件/网络发送更常用）
- f-string：最推荐的格式化方式（含 `{var=}`、`!r`）
- 格式化规格：对齐、宽度、精度、千分位、百分比
- dict 输出：`k=v`、JSON、querystring
- `str` vs `repr`：理解对象打印机制（以及如何自定义）
- 常见坑：字符串拼接、join 非字符串、sep 必须是 str
- 旧代码兼容：`str.format()` / `%`（看得懂也改得动）

---

## 5) 逐个详解（怎么跑 + 学到什么）

下面每一节都能直接复制命令运行。

### 01 - `01_overview.py`

运行：
- `python3 01_Basics/03_Printing/01_overview.py`

你会学到：
- 快速浏览本目录的全部示例文件与主题

---

### 02 - `02_print_multiple_objects.py`（核心：一次 print 打多个内容）

运行：
- `python3 01_Basics/03_Printing/02_print_multiple_objects.py`

你会学到：
- `print(*objects, sep, end, flush)` 的所有关键参数
- 默认分隔符是空格；如何自定义分隔符
- `end` 如何让两次输出出现在同一行
- `print(obj)` 默认用 `str(obj)`，调试时如何输出 `repr(obj)`

---

### 03 - `03_unpacking_iterables.py`（print(*items)）

运行：
- `python3 01_Basics/03_Printing/03_unpacking_iterables.py`

你会学到：
- `print(items)` 打印容器；`print(*items)` 打印元素
- dict 的 `*` 解包得到 keys（不是 key=value）
- set 顺序不稳定：想要稳定输出用 `sorted(set)`

---

### 04 - `04_join_vs_sep.py`（join vs sep）

运行：
- `python3 01_Basics/03_Printing/04_join_vs_sep.py`

你会学到：
- `print(*items, sep=", ")` 对非字符串元素也能工作（print 会做 `str()`）
- `", ".join(...)` 要求元素都是 `str`（否则 TypeError）
- 想“得到字符串”而不是“直接打印”时，join 更合适

---

### 05 - `05_fstring_and_debug.py`（最推荐：f-string）

运行：
- `python3 01_Basics/03_Printing/05_fstring_and_debug.py`

你会学到：
- 一行输出多个字段：`f"name={name} age={age}"`
- 调试友好：`f"{name=} {age=}"`
- `!r` 输出更原始的形式（字符串带引号/转义）
- f-string 里直接写格式化规格（如小数位、对齐）

---

### 06 - `06_format_spec_mini_language.py`（对齐/精度/千分位）

运行：
- `python3 01_Basics/03_Printing/06_format_spec_mini_language.py`

你会学到：
- 打印表格行：列宽/对齐（更像“专业输出”）
- 数字千分位 `:,`、百分比 `.1%`、零填充等

---

### 07 - `07_print_dicts_key_values.py`（结构化输出）

运行：
- `python3 01_Basics/03_Printing/07_print_dicts_key_values.py`

你会学到：
- 一行 `k=v`（日志常用）
- 一行 JSON（机器更容易解析）
- 一行 querystring（URL 参数风格）

---

### 08 - `08_repr_str_and_custom_objects.py`（对象如何影响打印）

运行：
- `python3 01_Basics/03_Printing/08_repr_str_and_custom_objects.py`

你会学到：
- `print(obj)` 用 `__str__`
- `repr(obj)`/`!r` 用 `__repr__`
- 为什么“写好 __repr__”对调试很重要

---

### 09 - `09_same_line_update.py`（同一行刷新）

运行：
- `python3 01_Basics/03_Printing/09_same_line_update.py`

你会学到：
- 进度条/状态更新的常用写法：`\r` + `end=""` + `flush=True`
- 为什么不同终端对 `\r` 的表现可能不同（环境差异）

---

### 10 - `10_print_to_file_and_capture.py`（file= 与捕获输出）

运行：
- `python3 01_Basics/03_Printing/10_print_to_file_and_capture.py`

你会学到：
- `file=` 把输出写到任意文件/缓冲区
- `StringIO` 捕获 print 输出（测试/拼日志常用）
- 输出到 `sys.stderr`（区分正常输出和错误信息）

---

### 11 - `11_common_mistakes.py`（常见错误与正确写法）

运行：
- `python3 01_Basics/03_Printing/11_common_mistakes.py`

你会学到：
- 为什么 `"age=" + 20` 会报错，正确写法是什么
- 为什么 `",".join([1,2,3])` 会报错，正确写法是什么
- `sep` 不是字符串会报错
- 列表“展开打印”的正确姿势：`print(*items)`

---

### 12 - `12_format_method_and_percent.py`（旧格式化方式：format / %）

运行：
- `python3 01_Basics/03_Printing/12_format_method_and_percent.py`

你会学到：
- `str.format()`：位置填充与名字填充
- `format_map()`：用 dict 喂模板（很适合一行 key=value）
- `%`（printf 风格）：旧代码里常见，至少要看得懂

---

## 6) 最终总结：优先使用哪种方式？

按常用程度给一个简单排序（从推荐到备用）：

1) **f-string**：可读性最好，最推荐（`05_fstring_and_debug.py`）
2) **print + 多参数 + sep/end**：最直接（`02_print_multiple_objects.py`）
3) **`print(*items, sep=...)`**：打印可迭代对象元素很方便（`03_unpacking_iterables.py`）
4) **`"sep".join(...)`**：当你需要“得到字符串”再写日志/文件/网络时更合适（`04_join_vs_sep.py`）
5) **`str.format()` / `%`**：不再推荐写新代码用它，但要能看懂（`12_format_method_and_percent.py`）
