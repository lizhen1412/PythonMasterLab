# Python 3.11+ 文件与 CSV（Files & CSV）学习笔记（第 19 章）

本章是一组“可运行的小脚本”，讲解文件与 CSV 的核心能力：路径遍历、打开模式/编码/换行、文本/二进制读写、临时文件与安全写入、权限与错误处理、CSV 读写（reader/writer/DictReader/DictWriter）、dialect/quoting/Sniffer、流式处理与编码/BOM。附带练习题（每题一文件）。

---

## 1) 怎么运行

在仓库根目录执行：

- 先看索引：`python3 01_Basics/19_Files_and_CSV/01_overview.py`
- 运行某个示例：`python3 01_Basics/19_Files_and_CSV/02_paths_and_traversal.py`
- 练习题索引：`python3 01_Basics/19_Files_and_CSV/Exercises/01_overview.py`

---

## 2) 本章“知识点全景”清单

- 路径与遍历：`pathlib.Path` 拼接/exists/is_file/iterdir/glob/stat
- 打开与模式：`open` 的 mode/encoding/newline/buffering/errors；文本 vs 二进制
- 文本读写：逐行/分块、`seek/tell`、`flush`、错误处理
- 二进制读写：bytes/bytearray、偏移读取
- 临时文件与安全写：`tempfile`、写临时文件后替换
- 权限与错误：`stat` 元数据、`chmod`、`PermissionError/FileNotFoundError` 处理
- CSV 基础：`csv.reader/writer`，`newline=""`，`delimiter/quotechar/quoting`
- CSV 字典：`DictReader/DictWriter`，`writeheader`，缺失字段
- CSV dialect/quoting/Sniffer：自定义分隔符/引号，自动推断
- CSV 流式处理：迭代过滤/聚合，大文件不全量加载
- 编码与 BOM：`utf-8` vs `utf-8-sig`，空行/换行处理

---

## 3) 文件总览

| 编号 | 文件 | 一句话说明 |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | 本目录索引：列出全部示例与主题 |
| 02 | [`02_paths_and_traversal.py`](02_paths_and_traversal.py) | Path 基础、遍历、stat 元数据 |
| 03 | [`03_open_modes_and_context.py`](03_open_modes_and_context.py) | 打开模式/编码/newline/buffering，with/seek/tell |
| 04 | [`04_text_read_write_patterns.py`](04_text_read_write_patterns.py) | 文本读写：逐行/分块/错误处理 |
| 05 | [`05_binary_files_and_seek.py`](05_binary_files_and_seek.py) | 二进制读写、偏移读取、seek |
| 06 | [`06_temp_files_and_safe_write.py`](06_temp_files_and_safe_write.py) | tempfile、临时写后替换 |
| 07 | [`07_permissions_and_errors.py`](07_permissions_and_errors.py) | 权限/错误处理：stat、chmod、异常捕获 |
| 08 | [`08_csv_reader_writer_basics.py`](08_csv_reader_writer_basics.py) | csv.reader/writer 基础，newline="" |
| 09 | [`09_csv_dictreader_dictwriter.py`](09_csv_dictreader_dictwriter.py) | DictReader/DictWriter，writeheader、缺字段 |
| 10 | [`10_csv_quoting_and_dialect.py`](10_csv_quoting_and_dialect.py) | quoting/delimiter/quotechar，Sniffer |
| 11 | [`11_csv_streaming_and_filter.py`](11_csv_streaming_and_filter.py) | CSV 流式过滤/聚合，不全量加载 |
| 12 | [`12_csv_encoding_and_bom.py`](12_csv_encoding_and_bom.py) | 编码/BOM，空行处理 |
| 13 | [`13_chapter_summary.py`](13_chapter_summary.py) | 本章总结：规则清单与常见坑 |
| 14 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | 本章练习索引（每题一个文件） |

---

## 4) 本章练习（每题一个文件）

练习索引：`python3 01_Basics/19_Files_and_CSV/Exercises/01_overview.py`

- `Exercises/02_stream_count_lines.py`：逐行计数（大文件不全量读）
- `Exercises/03_binary_chunk_read.py`：二进制按块读取并统计长度
- `Exercises/04_dictreader_filter.py`：DictReader 过滤行并写出新文件
- `Exercises/05_handle_missing_columns.py`：处理缺失列/空行，容错输出
- `Exercises/06_sniffer_detect_dialect.py`：Sniffer 推断分隔符与是否有表头
- `Exercises/07_safe_overwrite.py`：安全写入：临时文件替换原文件
- `Exercises/08_permissions_error_handling.py`：捕获 FileNotFound/PermissionError
- `Exercises/09_bom_and_encoding.py`：读取带 BOM 的 CSV，并写回标准 UTF-8

---

## 5) 小贴士

- 文本模式处理 CSV 时记得 `newline=""`，否则可能出现空行
- 大文件优先逐行/分块处理，不要一次性读入
- 写文件失败要处理异常；必要时采用“写临时文件再替换”减少损坏风险
- CSV 字段缺失要设默认值或跳过，避免 KeyError
- UTF-8 一般无需 BOM，如遇 BOM 可用 `utf-8-sig` 读取并写回无 BOM 版本
