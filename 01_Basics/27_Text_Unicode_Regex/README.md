# Python 3.11+ Text, Unicode, and Regex (Chapter 27)

This chapter focuses on text handling beyond basic strings:
- Unicode normalization with unicodedata
- Encoding/decoding error strategies
- locale basics
- Regular expression advanced patterns

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/27_Text_Unicode_Regex/01_overview.py`
- Single lesson: `python3 01_Basics/27_Text_Unicode_Regex/02_unicode_normalization.py`
- Exercises index: `python3 01_Basics/27_Text_Unicode_Regex/Exercises/01_overview.py`

---

## 2) Key topics checklist

- NFC/NFD normalization
- encode/decode error modes: replace/ignore/backslashreplace
- locale info and formatting basics
- regex named groups, non-greedy, verbose mode

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_unicode_normalization.py`](02_unicode_normalization.py) | unicodedata normalization |
| 03 | [`03_encoding_errors.py`](03_encoding_errors.py) | encoding/decoding error strategies |
| 04 | [`04_locale_basics.py`](04_locale_basics.py) | locale basics |
| 05 | [`05_regex_compiled_groups.py`](05_regex_compiled_groups.py) | compiled regex with groups |
| 06 | [`06_regex_greedy_nongreedy.py`](06_regex_greedy_nongreedy.py) | greedy vs non-greedy |
| 07 | [`07_regex_verbose_flags.py`](07_regex_verbose_flags.py) | verbose patterns and flags |
| 08 | [`08_chapter_summary.py`](08_chapter_summary.py) | Summary |
| 09 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/27_Text_Unicode_Regex/Exercises/01_overview.py`

- `Exercises/02_normalized_equal.py`: Compare after normalization
- `Exercises/03_safe_decode.py`: Decode with error handling
- `Exercises/04_regex_extract_dates.py`: Extract dates with regex
- `Exercises/05_regex_find_emails.py`: Find emails
- `Exercises/06_regex_replace_tags.py`: Replace tags with non-greedy
