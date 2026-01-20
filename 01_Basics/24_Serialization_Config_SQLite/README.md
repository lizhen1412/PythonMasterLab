# Python 3.11+ Serialization, Config, and SQLite (Chapter 24)

This chapter covers common data serialization formats and local storage:
- JSON encoding/decoding and custom encoders
- Pickle roundtrip and security warning
- ConfigParser (INI-style config)
- tomllib (TOML)
- sqlite3 with in-memory database

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/24_Serialization_Config_SQLite/01_overview.py`
- Single lesson: `python3 01_Basics/24_Serialization_Config_SQLite/07_sqlite_in_memory_basics.py`
- Exercises index: `python3 01_Basics/24_Serialization_Config_SQLite/Exercises/01_overview.py`

---

## 2) Key topics checklist

- json.dumps / json.loads options (indent, ensure_ascii)
- Custom JSON encoder via default=
- Pickle is binary and unsafe for untrusted input
- configparser read_string / getint / getboolean
- tomllib.loads for TOML parsing (3.11+)
- sqlite3 in-memory database, parameterized queries

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_json_dumps_loads.py`](02_json_dumps_loads.py) | JSON dumps/loads basics |
| 03 | [`03_json_file_like_custom_encoder.py`](03_json_file_like_custom_encoder.py) | File-like JSON + custom encoder |
| 04 | [`04_pickle_roundtrip.py`](04_pickle_roundtrip.py) | Pickle roundtrip and warning |
| 05 | [`05_configparser_basics.py`](05_configparser_basics.py) | ConfigParser basics |
| 06 | [`06_tomllib_basics.py`](06_tomllib_basics.py) | TOML parsing with tomllib |
| 07 | [`07_sqlite_in_memory_basics.py`](07_sqlite_in_memory_basics.py) | sqlite3 in-memory usage |
| 08 | [`08_sqlite_row_factory_and_params.py`](08_sqlite_row_factory_and_params.py) | Row factory + parameterized queries |
| 09 | [`09_chapter_summary.py`](09_chapter_summary.py) | Summary |
| 10 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/24_Serialization_Config_SQLite/Exercises/01_overview.py`

- `Exercises/02_json_compact_line.py`: Compact JSON line
- `Exercises/03_pickle_roundtrip.py`: Pickle roundtrip
- `Exercises/04_configparser_get.py`: Read config with fallback
- `Exercises/05_tomllib_parse.py`: Parse TOML string
- `Exercises/06_sqlite_insert_count.py`: Insert and count rows
