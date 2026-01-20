# Python 3.11+ System, Debugging, and Testing (Chapter 25)

This chapter covers practical system tooling and debugging/testing basics:
- os/sys essentials and environment access
- shutil and tempfile for safe local operations
- subprocess basics
- signal handlers and atexit hooks
- logging with handlers/filters
- warnings and traceback utilities
- unittest basics
- timeit and cProfile for quick profiling

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/25_System_Debug_Testing/01_overview.py`
- Single lesson: `python3 01_Basics/25_System_Debug_Testing/08_unittest_basics.py`
- Exercises index: `python3 01_Basics/25_System_Debug_Testing/Exercises/01_overview.py`

---

## 2) Key topics checklist

- os/sys core info (cwd, argv, env)
- shutil + tempfile for safe temp work
- subprocess.run with capture_output
- signal and atexit for lifecycle hooks
- logging handlers, filters, and formatting
- warnings and traceback formatting
- unittest TestCase and TextTestRunner
- timeit and cProfile basics

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_os_sys_basics.py`](02_os_sys_basics.py) | os/sys essentials |
| 03 | [`03_shutil_tempfile_basics.py`](03_shutil_tempfile_basics.py) | shutil + tempfile |
| 04 | [`04_subprocess_basics.py`](04_subprocess_basics.py) | subprocess basics |
| 05 | [`05_signal_and_atexit.py`](05_signal_and_atexit.py) | signal + atexit |
| 06 | [`06_logging_handlers_and_filters.py`](06_logging_handlers_and_filters.py) | logging handlers/filters |
| 07 | [`07_warnings_and_traceback.py`](07_warnings_and_traceback.py) | warnings + traceback |
| 08 | [`08_unittest_basics.py`](08_unittest_basics.py) | unittest basics |
| 09 | [`09_timeit_and_cprofile.py`](09_timeit_and_cprofile.py) | timeit + cProfile |
| 10 | [`10_chapter_summary.py`](10_chapter_summary.py) | Summary |
| 11 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/25_System_Debug_Testing/Exercises/01_overview.py`

- `Exercises/02_get_env_default.py`: getenv with default
- `Exercises/03_subprocess_capture.py`: run Python and capture output
- `Exercises/04_warning_capture.py`: capture warnings
- `Exercises/05_traceback_last_line.py`: extract last traceback line
- `Exercises/06_unittest_small.py`: small unittest example
