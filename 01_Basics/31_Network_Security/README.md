# Python 3.11+ Network and Security Basics (Chapter 31)

This chapter covers non-networked examples of common modules:
- urllib.parse and request building
- hashlib and hmac
- ssl context basics

No external network access is required.

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/31_Network_Security/01_overview.py`
- Single lesson: `python3 01_Basics/31_Network_Security/02_urllib_parse_basics.py`
- Exercises index: `python3 01_Basics/31_Network_Security/Exercises/01_overview.py`

---

## 2) Key topics checklist

- urlparse, urlencode, parse_qs
- Request building without sending
- hashlib digest and hexdigest
- hmac with compare_digest
- ssl.create_default_context

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_urllib_parse_basics.py`](02_urllib_parse_basics.py) | URL parsing and encoding |
| 03 | [`03_urllib_request_build.py`](03_urllib_request_build.py) | Build Request objects |
| 04 | [`04_hashlib_basics.py`](04_hashlib_basics.py) | Hashing basics |
| 05 | [`05_hmac_basics.py`](05_hmac_basics.py) | HMAC basics |
| 06 | [`06_ssl_context_basics.py`](06_ssl_context_basics.py) | SSL context basics |
| 07 | [`07_chapter_summary.py`](07_chapter_summary.py) | Summary |
| 08 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/31_Network_Security/Exercises/01_overview.py`

- `Exercises/02_parse_query_params.py`: Parse query params
- `Exercises/03_build_query_url.py`: Build URL with query
- `Exercises/04_hash_password.py`: Compute sha256
- `Exercises/05_hmac_verify.py`: Verify HMAC
