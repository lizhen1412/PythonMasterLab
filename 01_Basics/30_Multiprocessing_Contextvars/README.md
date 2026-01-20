# Python 3.11+ Multiprocessing and Contextvars (Chapter 30)

This chapter covers process-based concurrency and context variables:
- multiprocessing.Process and Queue
- multiprocessing.Pool and ProcessPoolExecutor
- Manager for shared state
- contextvars for context isolation

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/30_Multiprocessing_Contextvars/01_overview.py`
- Single lesson: `python3 01_Basics/30_Multiprocessing_Contextvars/02_multiprocessing_process_basics.py`
- Exercises index: `python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/01_overview.py`

---

## 2) Key topics checklist

- Process basics and safe __main__ guard
- Queue/Pool/ProcessPoolExecutor
- Manager shared dict
- ContextVar and tokens

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_multiprocessing_process_basics.py`](02_multiprocessing_process_basics.py) | Process basics |
| 03 | [`03_multiprocessing_queue.py`](03_multiprocessing_queue.py) | Queue for results |
| 04 | [`04_process_pool_executor.py`](04_process_pool_executor.py) | ProcessPoolExecutor usage |
| 05 | [`05_manager_shared_dict.py`](05_manager_shared_dict.py) | Manager shared dict |
| 06 | [`06_contextvars_basics.py`](06_contextvars_basics.py) | ContextVar basics |
| 07 | [`07_chapter_summary.py`](07_chapter_summary.py) | Summary |
| 08 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/30_Multiprocessing_Contextvars/Exercises/01_overview.py`

- `Exercises/02_process_square_sum.py`: Sum of squares with processes
- `Exercises/03_process_pool_map.py`: ProcessPoolExecutor map
- `Exercises/04_manager_shared_counter.py`: Shared counter
- `Exercises/05_contextvar_token.py`: ContextVar set/reset
