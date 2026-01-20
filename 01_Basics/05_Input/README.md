# Python 3.11+ 输入（input）学习笔记

本章是一组“可运行的小脚本”，把 **Python 里所有常见的用户输入（stdin）场景** 一次讲清楚：`input()` 基础、空白处理、默认值、类型转换、一次输入多个值、输入校验与重试、多行输入、EOF/中断处理、`getpass` 密码输入、以及 `sys.stdin` 读取与“可测试的输入代码”写法。

---

## 1) 文件总览（先知道每个文件是干什么的）

建议按编号顺序学；每个文件都能单独运行。

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例及主题 |
| 02 | [`02_input_basics.py`](02_input_basics.py) | `input()` 基础：返回值、提示语、空输入、空白处理 |
| 03 | [`03_strip_and_default.py`](03_strip_and_default.py) | `.strip()` 与默认值：空输入/空白输入怎么处理 |
| 04 | [`04_type_conversions.py`](04_type_conversions.py) | 类型转换：int/float/Decimal/bool（含安全处理） |
| 05 | [`05_multiple_values_split.py`](05_multiple_values_split.py) | 一行输入多个值：split/unpack/map/shlex/csv |
| 06 | [`06_validation_loops.py`](06_validation_loops.py) | 校验与重试：范围检查、选择题、yes/no 默认值 |
| 07 | [`07_multiline_until_sentinel.py`](07_multiline_until_sentinel.py) | 多行输入：直到 END 结束 |
| 08 | [`08_eof_and_interrupt.py`](08_eof_and_interrupt.py) | EOFError / KeyboardInterrupt：优雅退出（不刷堆栈） |
| 09 | [`09_getpass_secret_input.py`](09_getpass_secret_input.py) | 密码输入：getpass（不回显；仅在 TTY 生效） |
| 10 | [`10_sys_stdin_readline_and_pipe.py`](10_sys_stdin_readline_and_pipe.py) | sys.stdin：readline/read/迭代到 EOF；配合管道 |
| 11 | [`11_testable_input_functions.py`](11_testable_input_functions.py) | 可测试输入：把 input 当依赖注入（fake_input） |
| 12 | [`12_structured_input_parsing.py`](12_structured_input_parsing.py) | 结构化输入：JSON / Python 字面量（安全解析） |
| 13 | [`13_cli_args_and_argparse.py`](13_cli_args_and_argparse.py) | 命令行参数：sys.argv 与 argparse |
| 14 | [`14_environment_variables.py`](14_environment_variables.py) | 环境变量输入：os.environ / os.getenv |
| 15 | [`15_stdin_binary_and_encoding.py`](15_stdin_binary_and_encoding.py) | 二进制 stdin：sys.stdin.buffer 与解码 |
| 16 | [`16_fileinput_multiple_sources.py`](16_fileinput_multiple_sources.py) | 多来源输入：fileinput 统一处理文件与 stdin |
| 17 | [`17_readline_history_and_completion.py`](17_readline_history_and_completion.py) | readline：历史记录与补全（平台可选） |
| 18 | [`18_nonblocking_and_timeout_input.py`](18_nonblocking_and_timeout_input.py) | 非阻塞/超时输入：select 等待 stdin |

---

## 2) 怎么运行（小白版）

下面命令都以“仓库根目录”为当前工作目录（也就是你能看到 `01_Basics/` 的那一层）：

- 先看索引：`python3 01_Basics/05_Input/01_overview.py`
- 运行某个示例：`python3 01_Basics/05_Input/02_input_basics.py`

> 这一章的脚本大多会等待你输入内容：跟着终端提示输入即可。  
> 想结束输入：macOS/Linux 通常用 Ctrl-D；Windows 通常用 Ctrl-Z 后回车；中断用 Ctrl-C。

---

## 3) 你要掌握的知识点（Checklist）

- `input(prompt)` 永远返回 **str**
- input 读取“一行”，并移除结尾换行符（不会自动 strip 空白）
- 空输入：直接回车 -> `""`（空字符串）
- `.strip()`：清理前后空白；配合 `or default` 做默认值
- 类型转换：`int()` / `float()` / `Decimal()`；失败会 `ValueError`（要捕获）
- 解析 bool：需要自己规定规则（y/n、true/false、1/0）
- 一行多个值：`split()` + 解包；必要时 `shlex.split`/`csv`
- 校验与重试：while True 循环直到输入合法
- 多行输入：循环 `input()` 直到哨兵（END）或 EOF
- EOFError / KeyboardInterrupt：要“优雅退出”，不要堆栈刷屏
- 密码输入：`getpass.getpass()`（需要终端 TTY）
- 读取到 EOF：`for line in sys.stdin:`（适合管道/重定向）
- 工程写法：把 `input()` 当依赖注入，让逻辑可测试
- 结构化输入：`json.loads` / `ast.literal_eval`（安全解析成 list/dict）
- 命令行参数：`sys.argv` / `argparse`
- 环境变量：`os.environ` / `os.getenv`
- 二进制 stdin：`sys.stdin.buffer`
- 多来源输入：`fileinput`
- 行编辑/历史：`readline`
- 超时/非阻塞：`select`

---

## 4) 逐个详解（怎么跑 + 学到什么）

### 01 - `01_overview.py`

运行：
- `python3 01_Basics/05_Input/01_overview.py`

它做什么：
- 列出本目录所有示例文件，并标记 `OK/MISSING`

---

### 02 - `02_input_basics.py`

运行：
- `python3 01_Basics/05_Input/02_input_basics.py`

你会学到：
- `input()` 的返回值类型、空输入、空白处理（`strip`）

可以试试：
- 第 1 问输入：`Alice`
- 第 2 问输入：`  hi  `
- 第 3 问直接回车

---

### 03 - `03_strip_and_default.py`

运行：
- `python3 01_Basics/05_Input/03_strip_and_default.py`

你会学到：
- `value = input(...).strip() or "default"` 这种“默认值”写法
- `strip/lstrip/rstrip` 的区别

可以试试：
- 直接回车（会用默认值）
- 输入：`   Bob   `（会被 strip 成 `Bob`）

---

### 04 - `04_type_conversions.py`

运行：
- `python3 01_Basics/05_Input/04_type_conversions.py`

你会学到：
- 把 input 得到的 str 转成 int/float/Decimal/bool
- 转换失败时怎么处理（捕获异常、回退默认值）

可以试试：
- 年龄输入：`abc`（会回退默认 18）
- 分数输入：`98.5`
- 价格输入：`19.99`
- 是否继续输入：`y`

---

### 05 - `05_multiple_values_split.py`

运行：
- `python3 01_Basics/05_Input/05_multiple_values_split.py`

你会学到：
- 一行输入多个字段：`split` + 解包
- 引号场景：`shlex.split`
- 逗号分隔：简单 split；复杂用 `csv`

可以试试：
- 第 1 问输入：`10 20`
- 第 2 问输入：`Alice,Bob,Charlie`
- 第 3 问输入：`name="Alice Bob" city=Beijing`
- 第 4 问输入：`hello world this is comment`

---

### 06 - `06_validation_loops.py`

运行：
- `python3 01_Basics/05_Input/06_validation_loops.py`

你会学到：
- “必须输入合法值”的专业写法：循环提示直到合法
- 范围检查 / 选择题 / yes-no（含默认值）

可以试试：
- 年龄先输入 `200` 再输入 `20`（看范围校验）
- 难度输入 `4` 再输入 `2`
- 提交时直接回车（默认 False）

---

### 07 - `07_multiline_until_sentinel.py`

运行：
- `python3 01_Basics/05_Input/07_multiline_until_sentinel.py`

你会学到：
- 多行输入：循环读行，直到输入 `END`

可以试试：
- 连续输入几行文本，最后输入一行 `END`

---

### 08 - `08_eof_and_interrupt.py`

运行：
- `python3 01_Basics/05_Input/08_eof_and_interrupt.py`

你会学到：
- EOFError / KeyboardInterrupt 的含义与处理方式
- 如何优雅退出（不刷堆栈）

可以试试：
- 输入几行，然后输入 `quit`
- 或者按 Ctrl-D / Ctrl-Z / Ctrl-C 体验退出方式

---

### 09 - `09_getpass_secret_input.py`

运行：
- `python3 01_Basics/05_Input/09_getpass_secret_input.py`

你会学到：
- `getpass.getpass()`：不回显输入，更适合密码/密钥
- 为什么它需要 TTY（非交互环境会退化/告警）

可以试试：
- 输入任意密码，观察脚本只输出长度与掩码（不会打印明文）

---

### 10 - `10_sys_stdin_readline_and_pipe.py`

运行：
- `python3 01_Basics/05_Input/10_sys_stdin_readline_and_pipe.py`

你会学到：
- `sys.stdin.readline/read` 到 EOF 的行为（返回 `""`）
- `input()` 与 `readline()` 的核心差异（是否自动去掉 `\\n` / EOF 行为不同）
- 专业小技巧：prompt 写到 stderr（stdout 可保持干净用于管道/重定向）

可以试试：
- 交互模式下按提示输入一行，观察 `readline()` 返回值包含 `\\n`（用 repr 能看出来）

---

### 11 - `11_testable_input_functions.py`

运行：
- `python3 01_Basics/05_Input/11_testable_input_functions.py`

你会学到：
- 把 `input()` 当“依赖”传入函数：让业务逻辑可测试、可复用
- 用 fake_input 模拟用户输入（不用敲键盘也能验证逻辑）

可以试试：
- 先看脚本自动跑的 fake_input，再自己在第二段交互里输入 name/age

---

### 12 - `12_structured_input_parsing.py`

运行：
- `python3 01_Basics/05_Input/12_structured_input_parsing.py`

你会学到：
- 从一行字符串解析出 list/dict：JSON（`json.loads`）与 Python 字面量（`ast.literal_eval`）
- 为什么不要对用户输入用 `eval()`

可以试试：
- 第一段直接回车（用默认 JSON），或者输入：`[1, 2, 3]`
- 第二段直接回车（用默认字面量），或者输入：`{"a": 1, "b": [2, 3]}`

---

### 13 - `13_cli_args_and_argparse.py`

运行：
- `python3 01_Basics/05_Input/13_cli_args_and_argparse.py --name Alice --count 2 hello world`

你会学到：
- `sys.argv` 的原始参数列表
- `argparse` 的解析、默认值与类型转换

---

### 14 - `14_environment_variables.py`

运行：
- `python3 01_Basics/05_Input/14_environment_variables.py`

你会学到：
- `os.environ` / `os.getenv` 读取环境变量
- 解析 int/bool 的常见写法

---

### 15 - `15_stdin_binary_and_encoding.py`

运行：
- `python3 01_Basics/05_Input/15_stdin_binary_and_encoding.py`
- `printf "hello\n" | python3 01_Basics/05_Input/15_stdin_binary_and_encoding.py`

你会学到：
- `sys.stdin.buffer` 二进制读取
- 手动 decode 处理编码

---

### 16 - `16_fileinput_multiple_sources.py`

运行：
- `python3 01_Basics/05_Input/16_fileinput_multiple_sources.py`

你会学到：
- `fileinput` 统一处理文件与 stdin
- `fileinput.filename()` / `filelineno()` 获取来源信息

---

### 17 - `17_readline_history_and_completion.py`

运行：
- `python3 01_Basics/05_Input/17_readline_history_and_completion.py`

你会学到：
- `readline` 的历史记录与补全（平台可选）

---

### 18 - `18_nonblocking_and_timeout_input.py`

运行：
- `python3 01_Basics/05_Input/18_nonblocking_and_timeout_input.py`

你会学到：
- `select` 实现超时输入（Windows 有限制）

## 5) 最终总结（你学完后应该能回答的问题）

- 为什么 `input()` 永远返回 str？为什么必须自己做类型转换？
- 空输入/空白输入怎么区分？默认值怎么写最简洁？
- 如何安全地把输入转换成 int/float/Decimal/bool（转换失败不崩）？
- 一行输入多个字段怎么解析？引号/逗号的场景怎么处理？
- 为什么要写“校验 + 重试”的循环？如何优雅处理 EOF/Ctrl-C？
- `getpass` 和 `input` 有什么区别？为什么 getpass 需要 TTY？
- `input()` 和 `sys.stdin.readline()` 的差异是什么？什么时候用 `for line in sys.stdin`？
- 如何把输入逻辑写得可测试（不依赖手动敲键盘）？
- 如果用户输入的是 JSON 或 list/dict 字面量，你该如何安全解析？
