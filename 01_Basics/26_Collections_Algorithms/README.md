# Python 3.11+ Collections and Algorithms (Chapter 26)

This chapter covers small but powerful standard library tools:
- heapq for priority queues
- bisect for binary search and insertion
- array for compact numeric storage
- struct for binary packing/unpacking
- enum for named constants
- collections.abc for protocol-style checks

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/26_Collections_Algorithms/01_overview.py`
- Single lesson: `python3 01_Basics/26_Collections_Algorithms/02_heapq_basics.py`
- Exercises index: `python3 01_Basics/26_Collections_Algorithms/Exercises/01_overview.py`

---

## 2) Key topics checklist

- heapq: heapify, heappush, heappop, nlargest/nsmallest
- bisect: bisect_left/right, insort
- array: typed storage, tolist, buffer_info
- struct: pack/unpack with format strings
- enum: Enum, IntEnum, Flag
- collections.abc: Iterable/Sequence/Mapping checks

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_heapq_basics.py`](02_heapq_basics.py) | heapq basics and priority queue |
| 03 | [`03_bisect_basics.py`](03_bisect_basics.py) | bisect and insort |
| 04 | [`04_array_basics.py`](04_array_basics.py) | array module basics |
| 05 | [`05_struct_basics.py`](05_struct_basics.py) | struct pack/unpack |
| 06 | [`06_enum_basics.py`](06_enum_basics.py) | Enum, IntEnum, Flag |
| 07 | [`07_collections_abc_basics.py`](07_collections_abc_basics.py) | collections.abc checks |
| 08 | [`08_chapter_summary.py`](08_chapter_summary.py) | Summary |
| 09 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/26_Collections_Algorithms/Exercises/01_overview.py`

- `Exercises/02_heapq_top_k.py`: Top-k using heapq
- `Exercises/03_bisect_insert_sorted.py`: Insert into sorted list
- `Exercises/04_array_average.py`: Average from array
- `Exercises/05_struct_parse_header.py`: Parse bytes with struct
- `Exercises/06_enum_status_parse.py`: Parse enum status
- `Exercises/07_collections_abc_is_sequence.py`: Sequence check
