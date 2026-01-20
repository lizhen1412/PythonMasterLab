# Python 3.11+ 异常处理（Exception Handling）学习笔记（第 13 章）

本章聚焦：异常是什么、常见错误、内置异常总览、`try` 语句、`raise` 的多种用法、用 `logging` 做调试，以及一个“简单计算器”示例。最后提供练习题（每题一个文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/13_Exception_Handling/01_overview.py`
- 运行某个示例：`python3 01_Basics/13_Exception_Handling/08_simple_calculator.py`
- 练习题索引：`python3 01_Basics/13_Exception_Handling/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单（按主题枚举）

### 2.1 异常是什么（以及怎么读 Traceback）

- **SyntaxError/IndentationError**：解析/编译阶段错误，通常靠“改代码”解决（不是靠 try/except）。
- **Exception（运行时异常）**：运行过程中出现的问题，会打印 **traceback（调用栈）**。
- 读 traceback 的要点：从上到下是调用链；**最后一行**是异常类型与消息；回到对应行定位根因。

### 2.2 异常处理的基本原则

- 优先修复根因，不要用 `try/except` 掩盖 bug。
- **只捕获你能处理的异常**：能恢复/能给出更清晰提示/能清理资源。
- 典型做法：`except Exception as exc:`，避免无脑 `except:`（会把 `KeyboardInterrupt/SystemExit` 也吞掉）。

### 2.3 异常（错误）类型：常见的你必须认识

- `NameError`：变量未定义
- `TypeError`：类型不匹配（如 `1 + "2"`）
- `ValueError`：值不合法（如 `int("abc")`）
- `IndexError` / `KeyError`：索引/字典 key 不存在
- `AttributeError`：对象没有某属性/方法
- `ZeroDivisionError`：除 0
- `FileNotFoundError` / `PermissionError`：文件路径/权限问题
- `ImportError` / `ModuleNotFoundError`：导入失败

### 2.4 “全部内置异常”与异常体系（Python 3.11+）

- 顶层：`BaseException`（包含 `SystemExit/KeyboardInterrupt/GeneratorExit` 等“不建议捕获”的异常）
- 常规异常：`Exception`（业务代码通常只捕获这一支）
- Python 3.11+：`ExceptionGroup` / `BaseExceptionGroup` 与 `except*`（批量错误处理）

### 2.5 `try` 语句：写法枚举（都要会）

- `try/except`：捕获并处理
- 多分支捕获：多个 `except`（**先具体后泛化**）
- `except (TypeError, ValueError) as exc:`：一次捕获多种类型
- `try/except/else`：`else` 仅在“无异常”时运行（把成功路径放到 else 更清晰）
- `try/except/finally` 或 `try/finally`：`finally` **一定执行**（清理资源/回收状态）

### 2.6 `raise` 关键字：常用套路

- 主动抛错：`raise ValueError("...")`
- 重新抛出（保留原 traceback）：`raise`
- 异常链：`raise NewError(...) from exc`
- 抑制上下文：`raise NewError(...) from None`（让错误信息更聚焦）
- 自定义异常：用更贴近业务的异常名表达语义

### 2.7 代码调试（日志 logging）

- 用 `logging` 的 `DEBUG/INFO/WARNING/ERROR` 等级代替满屏 `print`
- 在 `except` 里用 `logger.exception(...)` 打印带 traceback 的日志

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_exception_handling_basics.py`](02_exception_handling_basics.py) | 异常是什么：traceback、能/不能 catch 的区别 |
| 03 | [`03_common_errors.py`](03_common_errors.py) | 常见错误演示：NameError/TypeError/... |
| 04 | [`04_all_builtin_exceptions.py`](04_all_builtin_exceptions.py) | 列出并展示内置异常体系（含 3.11+ ExceptionGroup） |
| 05 | [`05_try_statement_patterns.py`](05_try_statement_patterns.py) | try 语句各种写法：except/else/finally/except* |
| 06 | [`06_raise_keyword_patterns.py`](06_raise_keyword_patterns.py) | raise 的多种用法：from / from None / re-raise / 自定义异常 |
| 07 | [`07_logging_debugging.py`](07_logging_debugging.py) | logging 调试：分级日志 + 打印 traceback |
| 08 | [`08_simple_calculator.py`](08_simple_calculator.py) | 简单计算器：解析表达式 + 异常处理（可选 REPL） |
| 09 | [`09_chapter_summary.py`](09_chapter_summary.py) | 本章总结：关键规则 + 常见误区清单 |
| 10 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/13_Exception_Handling/Exercises/01_overview.py`

- `Exercises/02_safe_divide.py`：安全除法：处理 0 和非法参数
- `Exercises/03_parse_int_strict.py`：严格解析 int：自定义错误信息 + 异常链
- `Exercises/04_validate_age_raise.py`：用 raise 做参数校验（ValueError/TypeError）
- `Exercises/05_read_first_line_try_finally.py`：try/finally 做资源清理（示例含清理临时文件）
- `Exercises/06_custom_exception_withdraw.py`：自定义异常：余额不足
- `Exercises/07_reraise_and_from_none.py`：re-raise 与 from None 的对比
- `Exercises/08_logging_exception_helper.py`：用 logging.exception 记录错误
- `Exercises/09_simple_calculator_core.py`：实现计算器核心函数（不使用 eval）
- `Exercises/10_retry_until_success.py`：失败重试：捕获异常并在最后抛出
- `Exercises/11_exception_group_parse_many.py`：进阶：ExceptionGroup + except*（Py 3.11+）

