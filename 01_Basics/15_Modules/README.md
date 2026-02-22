# Python 3.11+ 模块与包（Modules & Packages）学习笔记（第 15 章）

本章是一组"可运行的小脚本"，讲解模块/包的导入与使用、常用标准库（`random`/`re`/`datetime`/`turtle`/`socket`）、实用小示例（随机小游戏、身份证号校验、TCP/UDP 网络编程），以及如何安装第三方库（pip/venv/uv/pipx）。附带练习题（每题一文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/15_Modules/01_overview.py`
- 运行某个示例：`python3 01_Basics/15_Modules/04_random_basics.py`
- 练习题索引：`python3 01_Basics/15_Modules/Exercises/01_overview.py`

---

## 2) 本章"知识点全景"清单

### 2.1 模块与包
- `import` / `from ... import ...` / `as` 重命名；`__name__` 与脚本/模块模式
- 导入路径（`sys.path`）、相对导入（仅包内有效）、`__init__.py` 的作用
- `__all__` 控制 `from pkg import *`；懒导入的常见场景

### 2.2 常用标准库与示例
- `random`：随机数、打乱、采样；随机小游戏（猜数字）
- `re`：编译/搜索/分组；身份证号校验（长度 + 出生日期 + 校验码）
- 时间日期：`datetime`/`timezone`/`strftime`；`time` 睡眠与时间戳
- `turtle`：绘图入门（需要图形界面，示例内置安全检查）
- `socket`：TCP/UDP 服务器客户端、套接字选项、非阻塞 I/O、select 多路复用
- `importlib.resources`：读取包内资源文件
- `secrets`：安全随机（对比 random 的非安全性）

### 2.3 安装第三方库（文档）
- `python -m venv` 创建虚拟环境；`pip install ...`
- `uv pip install ...`、`uv venv .venv`（更快的安装器）
- `pipx` 隔离安装 CLI 工具
- 常见问题：国内镜像、权限、版本查看/卸载
- `requirements.txt` / 约束文件的常见用法（文档中补充）

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_import_basics.py`](02_import_basics.py) | 模块导入基础：import/from/as、`__name__` 与脚本入口 |
| 03 | [`03_package_structure_and_init.py`](03_package_structure_and_init.py) | 包结构、`__init__.py`、相对导入与 `__all__` 讲解 |
| 04 | [`04_random_basics.py`](04_random_basics.py) | random：取数、打乱、采样、种子 |
| 05 | [`05_random_guessing_game.py`](05_random_guessing_game.py) | 随机小游戏：猜数字（模拟输入） |
| 06 | [`06_regex_basics.py`](06_regex_basics.py) | 正则基础：编译、搜索、分组、替换 |
| 07 | [`07_id_card_validation.py`](07_id_card_validation.py) | 身份证号校验：格式 + 出生日期 + 校验码 |
| 08 | [`08_datetime_and_time.py`](08_datetime_and_time.py) | 日期时间：now/utc/格式化/解析/时间戳 |
| 09 | [`09_turtle_basics.py`](09_turtle_basics.py) | turtle 绘图入门（需图形界面，内置安全跳过） |
| 10 | [`10_socket_basics.py`](10_socket_basics.py) | socket 基础：地址族/类型，socketpair 本地收发演示 |
| 11 | [`11_installing_third_party_packages.md`](11_installing_third_party_packages.md) | 文档：pip/venv/uv/pipx 安装第三方库指南 |
| 12 | [`12_chapter_summary.py`](12_chapter_summary.py) | 本章总结：规则清单与常见坑 |
| 13 | [`13_package_main_and_reload.py`](13_package_main_and_reload.py) | 包入口（`-m`/`__main__.py`）与模块缓存/reload |
| 14 | [`14_importing_resources.py`](14_importing_resources.py) | importlib.resources 读取包内数据文件 |
| 15 | [`15_secrets_vs_random.py`](15_secrets_vs_random.py) | 安全随机：secrets vs random |
| 16 | [`16_tcp_server_client.py`](16_tcp_server_client.py) | TCP 服务器与客户端：bind/listen/accept/connect |
| 17 | [`17_udp_server_client.py`](17_udp_server_client.py) | UDP 服务器与客户端：sendto/recvfrom 数据报 |
| 18 | [`18_socket_options_timeout.py`](18_socket_options_timeout.py) | Socket 选项与超时：SO_REUSEADDR/KEEPALIVE/NODELAY |
| 19 | [`19_socket_nonblocking.py`](19_socket_nonblocking.py) | 非阻塞 Socket 与 select I/O 多路复用基础 |
| 20 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/15_Modules/Exercises/01_overview.py`

- `Exercises/02_inspect_import_paths.py`：查看/修改 `sys.path`，理解导入搜索顺序
- `Exercises/03_random_dice_simulation.py`：模拟掷骰子，统计频率
- `Exercises/04_regex_extract_emails.py`：用正则提取邮箱地址
- `Exercises/05_validate_id_cards.py`：批量校验身份证号（调用章节函数）
- `Exercises/06_socket_echo_with_socketpair.py`：用 `socket.socketpair` 实现本地 echo

---

## 5) 小贴士

- 运行脚本时保持当前工作目录在仓库根，确保相对路径和导入正常
- `if __name__ == "__main__": ...` 用于"脚本入口"，被 import 时不会自动执行
- 没有图形界面的环境（如远程服务器）运行 `turtle` 需提前检查/跳过
- TCP/UDP 示例使用 localhost 避免网络问题和防火墙干扰
- 生产环境网络编程需考虑异常处理、并发连接、优雅关闭等
