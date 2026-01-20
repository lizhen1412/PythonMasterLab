# Python 3.11+ 注释（Comments）学习笔记

这个目录是一组“可运行的小脚本”，用来把 **Python 注释相关的所有核心知识点** 一次讲清楚：普通 `#` 注释、块注释、docstring、类型注释（`# type: ...`）、编码声明、shebang、工具指令注释，以及用 `tokenize`/`ast` 视角理解它们。

---

## 1) 文件总览（先知道每个文件是干什么的）

建议按编号顺序学；每个文件都能单独运行。

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例及主题 |
| 02 | [`02_single_line.py`](02_single_line.py) | 单行注释与行尾注释（`#` 的基础规则） |
| 03 | [`03_inline_and_joining.py`](03_inline_and_joining.py) | 行尾注释规范 + 换行方式：括号隐式换行 vs 反斜杠续行坑 |
| 04 | [`04_block_comments.py`](04_block_comments.py) | 块注释（连续多行 `#`）的写法与使用场景 |
| 05 | [`05_docstrings_basics.py`](05_docstrings_basics.py) | docstring 基础：模块/类/函数，`__doc__`/`inspect.getdoc()` |
| 06 | [`06_docstring_vs_string_literal.py`](06_docstring_vs_string_literal.py) | docstring 和“三引号字符串表达式”的区别（含反汇编观察） |
| 07 | [`07_type_comments.py`](07_type_comments.py) | 类型注释：`# type: ...` 与 `# type: ignore`，以及 AST 视角 |
| 08 | [`08_encoding_cookie.py`](08_encoding_cookie.py) | 编码声明注释（coding cookie）：规则 + 检测 |
| 09 | [`09_shebang.py`](09_shebang.py) | shebang（`#!`）：让操作系统选择解释器（对 Python 来说仍是注释） |
| 10 | [`10_tooling_directives.py`](10_tooling_directives.py) | 工具指令注释：`# noqa` / `# fmt: off` / `# pragma: no cover` 等 |
| 11 | [`11_tokenize_extract_comments.py`](11_tokenize_extract_comments.py) | 用 `tokenize` 从源码提取普通注释 |
| 12 | [`12_ast_comments_and_docstrings.py`](12_ast_comments_and_docstrings.py) | AST 里看不到普通注释；docstring/type_comment 例外 |
| 13 | [`13_commenting_out_code_pitfalls.py`](13_commenting_out_code_pitfalls.py) | 用三引号“注释掉代码”的坑与替代方案 |

---

## 2) 逐个详解（小白版：怎么运行 + 学到什么）

### 通用运行方式（所有文件都适用）

下面命令都以“仓库根目录”为当前工作目录（也就是你看到 `01_Basics/` 的那一层）：

- 运行单个脚本：`python3 01_Basics/01_Comments/02_single_line.py`

Windows 上如果没有 `python3`，可尝试：

- `python 01_Basics/01_Comments/02_single_line.py`
- 或 `py -3.11 01_Basics/01_Comments/02_single_line.py`

> 你会在每个脚本末尾看到这段固定写法：`if __name__ == "__main__": main()`  
> 含义：当文件被“直接运行”时才执行 `main()`；当它被 `import` 时不会自动执行（方便复用/测试）。

---

### 01 - `01_overview.py`

运行：
- `python3 01_Basics/01_Comments/01_overview.py`

它做什么：
- 打印当前目录位置，并列出本目录全部示例文件
- 逐个检查文件是否存在（会标记 `OK/MISSING`）

你应该掌握：
- “学习目录应该先有索引”：让人一眼知道学什么、从哪开始

---

### 02 - `02_single_line.py`（单行注释 / 行尾注释）

运行：
- `python3 01_Basics/01_Comments/02_single_line.py`

核心知识点：
- **Python 真正的“注释”语法只有一种：`#` 到行末**
- `#` 出现在字符串里不算注释（例如 `"# not a comment"`）
- 行尾注释（写在代码后面）通常与代码间隔 **至少两个空格**（PEP 8 常用习惯）

你应该掌握：
- 什么时候用行尾注释：适合简短补充，不要写成“另一份代码”

---

### 03 - `03_inline_and_joining.py`（换行方式与注释的关系）

运行：
- `python3 01_Basics/01_Comments/03_inline_and_joining.py`

核心知识点：
- **括号隐式换行**：在 `()[]{}` 内换行是“语法允许的”，非常适合配合注释（列表/字典/长表达式）
- **反斜杠续行（`\\`）**：要求反斜杠必须是“这一行最后一个字符”，因此像 `\\  # comment` 这种写法会直接语法错误

你应该掌握：
- 长表达式优先用括号隐式换行；尽量少用反斜杠续行

---

### 04 - `04_block_comments.py`（块注释：连续多行 `#`）

运行：
- `python3 01_Basics/01_Comments/04_block_comments.py`

核心知识点：
- “块注释”不是语法结构，只是 **多行单行注释的组合**
- 好注释更偏向解释：**为什么这么做 / 有什么约束 / 有什么坑**，而不是复述“代码做了什么”

你应该掌握：
- 块注释要和代码保持同步；过期注释比没有注释更糟

---

### 05 - `05_docstrings_basics.py`（docstring：会进入运行时）

运行：
- `python3 01_Basics/01_Comments/05_docstrings_basics.py`

先记住一句话：
- **docstring 不是 `#` 注释**；它是“字符串字面量”，但因为位置特殊（作为模块/类/函数体的第一条语句）被 Python 当作文档。

核心知识点：
- `__doc__`：对象的 docstring 存放位置
- `help()` / `inspect.getdoc()`：读取 docstring 的常用方式
- `python -OO`：会移除 docstring（所以不要把业务逻辑写进 docstring 里）

你应该掌握：
- 什么时候写 docstring：对外暴露的模块/类/函数，描述用途、参数、返回值、异常等

---

### 06 - `06_docstring_vs_string_literal.py`（三引号字符串表达式 ≠ 注释）

运行：
- `python3 01_Basics/01_Comments/06_docstring_vs_string_literal.py`

核心知识点：
- 只有“第一条语句”的字符串才是 docstring
- 其它位置的三引号字符串只是一个“无用表达式语句”，会被编译进字节码（可以用 `dis` 看到）

你应该掌握：
- 不要用三引号字符串当注释来“屏蔽代码”（见 13 的坑）

---

### 07 - `07_type_comments.py`（类型注释 / 忽略注释）

运行：
- `python3 01_Basics/01_Comments/07_type_comments.py`

核心知识点（先建立正确预期）：
- `# type: ...` 和 `# type: ignore` 主要给 **静态类型检查器**（mypy/pyright 等）看
- **运行时不会强制类型**：写了类型注释也不会让 Python 自动报错或自动转换

本文件覆盖：
- 推荐写法：类型注解 `values: list[int]`、`def add(a: int, b: int) -> int`
- 旧写法（放在“源码字符串示例”里展示）：`# type: ...`（变量/函数签名/`lambda` 场景）
- 忽略指令（同样在源码字符串里展示）：`# type: ignore`
- AST 视角：`ast.parse(..., type_comments=True)` 查看 `Assign.type_comment` / `FunctionDef.type_comment` / `Module.type_ignores`

你应该掌握：
- 类型注释是“工程工具链”一部分：对学习者来说先理解概念即可，不必强行在所有代码里使用

---

### 08 - `08_encoding_cookie.py`（编码声明注释）

运行：
- `python3 01_Basics/01_Comments/08_encoding_cookie.py`

核心知识点：
- `# coding: <encoding>` 必须出现在第 1 行或第 2 行（第 1 行为 shebang 的情况）
- Python 3 默认源码编码是 UTF-8，所以大多数项目不需要写
- 但它仍然是标准机制：解释器/tokenize 会用它来识别源码编码

你应该掌握：
- 遇到历史老项目/非 UTF-8 文件时，知道“该从哪里入手”

---

### 09 - `09_shebang.py`（shebang：对 OS 有意义）

运行（两种）：
- 直接用解释器运行：`python3 01_Basics/01_Comments/09_shebang.py`
- 在 macOS/Linux 上（可选）：`chmod +x 01_Basics/01_Comments/09_shebang.py && ./01_Basics/01_Comments/09_shebang.py`

核心知识点：
- shebang 的作用对象是 **操作系统**：让系统知道用哪个解释器运行脚本
- 对 Python 解释器来说，`#!...` 这一行仍然只是注释

你应该掌握：
- 脚本要想 `./xxx.py` 运行：需要 shebang + 可执行权限

---

### 10 - `10_tooling_directives.py`（工具指令注释）

运行：
- `python3 01_Basics/01_Comments/10_tooling_directives.py`

核心知识点：
- 这些注释对解释器没意义，但很多工程工具会读取它们
- 常见例子：
  - `# noqa`：忽略 lint 报警（ruff/flake8 等）
  - `# fmt: off/on`：控制格式化工具（black 等）
  - `# isort: skip`：控制 import 排序工具
  - `# pylint: disable=...`：控制 pylint
  - `# pragma: no cover`：控制 coverage 统计

你应该掌握：
- 是否生效取决于你有没有安装对应工具，以及工具配置；脚本本身只是“演示写法”

---

### 11 - `11_tokenize_extract_comments.py`（tokenize 能读到注释）

运行：
- `python3 01_Basics/01_Comments/11_tokenize_extract_comments.py`

核心知识点：
- 普通注释不会进入运行时对象模型/AST
- 但在 **token 流** 里是可见的（`tokenize.COMMENT`），所以格式化、lint、静态分析工具能读到注释

你应该掌握：
- 当你要“写工具处理源码”时，`tokenize` 是常见入口

---

### 12 - `12_ast_comments_and_docstrings.py`（AST 看不到普通注释）

运行：
- `python3 01_Basics/01_Comments/12_ast_comments_and_docstrings.py`

核心知识点：
- 普通 `# ...` 注释不会变成 AST 节点
- docstring 可以用 `ast.get_docstring()` 读到
- `# type: ...` 在 `type_comments=True` 时可保留到 AST（例如 `Assign.type_comment`）

你应该掌握：
- 想在 AST 里拿到“注释内容”，一般不行；需要走 `tokenize`（见 11）

---

### 13 - `13_commenting_out_code_pitfalls.py`（别用三引号“注释掉代码”）

运行：
- `python3 01_Basics/01_Comments/13_commenting_out_code_pitfalls.py`

核心知识点：
- 用三引号把代码包起来，**不是注释**
  - 在“第一条语句”位置：可能变成 docstring（影响 `__doc__`）
  - 在其它位置：会进入常量表并作为无用表达式执行（见 06 的反汇编）

推荐替代方案：
- 最好的：删除代码（交给 Git 记录历史）
- 临时禁用：用多行 `#` 块注释（清晰、工具友好）

---

## 3) 最终总结（速查表）

### 3.1 注释相关概念怎么区分

- **普通注释（`# ...`）**：只存在于源码文本里；运行时对象/AST 默认看不到；工具可用 `tokenize` 读取。
- **docstring**：本质是字符串字面量，但因为位置特殊会被绑定到 `__doc__`；`help()` 能展示；`-OO` 会移除。
- **类型注释（`# type: ...`）**：给静态类型检查器使用；`ast.parse(..., type_comments=True)` 可保留到 AST。
- **忽略指令（`# type: ignore`）**：告诉类型检查器忽略这一行的类型问题；在 AST 里会出现在 `Module.type_ignores`（需要 `type_comments=True`）。
- **工具指令注释**：解释器不关心；是否生效取决于工具（ruff/black/isort/pylint/coverage）与配置。
- **编码声明 / shebang**：看起来像注释，但分别影响“源码如何解码”和“OS 如何选择解释器”，属于特殊用途行。

### 3.2 写注释的一个简单原则

- 注释优先回答：**为什么这样写？有什么约束？不这样写会踩什么坑？**
- 别用注释复述代码字面意思；代码改了注释没改会误导人
