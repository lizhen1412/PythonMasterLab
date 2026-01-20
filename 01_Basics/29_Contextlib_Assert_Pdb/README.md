# Python 3.11+ contextlib, assert, and pdb (Chapter 29)

This chapter covers practical control-flow tools:
- contextlib for context manager helpers
- ExitStack for dynamic cleanup
- assert and __debug__
- safe breakpoint usage

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/29_Contextlib_Assert_Pdb/01_overview.py`
- Single lesson: `python3 01_Basics/29_Contextlib_Assert_Pdb/02_contextmanager_basics.py`
- Exercises index: `python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/01_overview.py`

---

## 2) Key topics checklist

- contextmanager decorator and try/finally cleanup
- ExitStack for multiple context managers
- suppress and redirect_stdout helpers
- assert, __debug__, and -O behavior
- safe breakpoint usage without blocking

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_contextmanager_basics.py`](02_contextmanager_basics.py) | contextmanager basics |
| 03 | [`03_exitstack_basics.py`](03_exitstack_basics.py) | ExitStack usage |
| 04 | [`04_contextlib_helpers.py`](04_contextlib_helpers.py) | suppress and redirect_stdout |
| 05 | [`05_assert_and_debug.py`](05_assert_and_debug.py) | assert and __debug__ |
| 06 | [`06_breakpoint_safe.py`](06_breakpoint_safe.py) | safe breakpoint usage |
| 07 | [`07_chapter_summary.py`](07_chapter_summary.py) | Summary |
| 08 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/29_Contextlib_Assert_Pdb/Exercises/01_overview.py`

- `Exercises/02_timer_context.py`: contextmanager timer
- `Exercises/03_suppress_error.py`: suppress specific error
- `Exercises/04_exitstack_close.py`: ExitStack closes resources
- `Exercises/05_assert_positive.py`: assert positive input
