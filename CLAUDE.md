# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PythonMasterLab is a comprehensive Python learning curriculum with 760+ runnable lessons organized as a progressive educational path. Each lesson is a self-contained, executable script designed for "learn-by-running" pedagogy. The project covers fundamentals (31 topics in `01_Basics/`) and frameworks (`02_Frameworks/` with Pandas, NumPy, and Requests).

## Environment Setup

- **Python**: 3.11+ required (`.python-version` specifies 3.11)
- **Package manager**: Uses `uv` (modern Python package manager with `uv.lock`)
- **Dependencies**: numpy>=2.4.0, pandas>=2.3.3, requests>=2.32.3 (only needed for framework lessons)

Install dependencies:
```bash
uv sync              # Using uv
# or
pip install numpy pandas requests   # Using pip
```

Running with uv (recommended):
```bash
# uv run automatically uses the project's virtual environment
uv run 01_Basics/02_Variables/01_overview.py

# Or manually activate the venv first
source .venv/bin/activate  # Linux/macOS
python3 01_Basics/02_Variables/01_overview.py
```

## Running Lessons

Every topic follows a consistent structure. Run lessons directly as scripts:

```bash
# Topic index (shows all available lessons)
python3 01_Basics/02_Variables/01_overview.py

# Individual lesson
python3 01_Basics/02_Variables/02_variable_basics.py

# Framework lessons
python3 02_Frameworks/01_Pandas/01_overview.py

# Exercises (within topic directories)
python3 01_Basics/11_Loops/Exercises/01_overview.py

# Comprehensive exercises (aggregated from multiple topics)
python3 01_Basics/08_Exercises/01_overview.py
```

## Validation & Testing

This project has **no dedicated test suite**. Validation is done by running lessons directly:

```bash
# Syntax check all basics
python3 -m compileall 01_Basics

# Run individual lessons to verify output
python3 <path_to_lesson>
```

If adding tests, place under `tests/` with `test_*.py` naming using stdlib `unittest`.

## Project Structure

```
01_Basics/              # 31 core Python topics (01-31)
├── 01_Comments/
├── 02_Variables/        # Variables and printing variables
├── 03_Printing/
├── 04_Formatting/
├── 05_Input/
├── 06_Variables/        # Variable creation, modification, naming, types, scope
├── 07_Data_Types/
├── 08_Exercises/        # Comprehensive exercises aggregating topics 01-07
├── 09_Operators/
├── ...
├── 31_Network_Security/
└── Each topic contains:
    ├── README.md          # Comprehensive documentation (Chinese for basics, English for advanced)
    ├── 01_overview.py     # Topic index with lesson list and status
    ├── 02_*.py, 03_*.py   # Numbered lesson files (self-contained runnable scripts)
    └── Exercises/         # Practical coding challenges (if applicable)
        ├── 01_overview.py
        └── 02_*.py, 03_*.py

02_Frameworks/           # Framework-specific lessons
├── 01_Pandas/           # 73 lessons + 23 exercises
├── 02_Numpy/            # 42 lessons + 14 exercises
└── 03_Requests/         # 27 lessons + 12 exercises using httpbin.org
```

## Code Conventions

### File Structure Pattern
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Descriptive docstring explaining the concept.
Includes how to run and what to learn.
"""

def main() -> None:
    # Implementation
    pass

if __name__ == "__main__":
    main()
```

### Naming & Organization
- **Files**: `snake_case` with numeric prefixes for ordering (`01_overview.py`, `02_variable_basics.py`)
- **Functions/variables**: `snake_case`
- **Type annotations**: Required (Python 3.11+ style)
- **Indentation**: 4 spaces
- **Numeric prefixes**: Preserve ordering (`01_`, `02_`, etc.)

### Lesson Design Principles
- **Self-contained**: No cross-lesson dependencies; each runs independently
- **Executable**: Every lesson demonstrates a concept with visible output
- **Documented**: Comprehensive docstrings explaining what and why
- **Practical**: Include common pitfalls, best practices, and real-world patterns

## Documentation Language

- **Basics topics** (01-31): README.md files in Chinese
- **Framework topics**: README.md files in Chinese
- **Code comments**: English throughout
- **AGENTS.md**: English

## Key Architecture Patterns

### Progressive Learning Path
Topics are numbered 01-31 in logical sequence from basics to advanced:
- Early topics: Variables, printing, data types, operators
- **Note**: `02_Variables/` covers variables and printing variables; `06_Variables/` covers variable creation, modification, naming, types, and scope
- Mid topics: Loops, functions, OOP, files, classes
- Advanced topics: Async, coroutines, multiprocessing, contextvars, network security

### Topic Index Pattern
Each `01_overview.py`:
- Defines a `TOPICS` list: `list[tuple[str, str]]` where each tuple is `(filename, description)`
- Shows completion status (OK/MISSING) using `pathlib.Path.exists()`
- Prints directory path and lesson listing when run
- Lesson descriptions are in Chinese for basics topics, English for frameworks

### Exercise System
Two types of exercises:
1. **Topic-specific**: `Exercises/` subdirectory within each topic (e.g., `01_Basics/11_Loops/Exercises/`)
2. **Comprehensive**: `01_Basics/08_Exercises/` aggregates exercises for topics 01-07 (Comments through Data Types)

## Commits & Pull Requests

- **Subjects**: Short, imperative mood (e.g., "Add numpy indexing exercises", "Fix variable scoping example")
- **PR body**: Include summary, affected topic paths (e.g., `01_Basics/11_Loops/`), and validation commands used
- **Validation**: Run affected lessons or `compileall` before committing

## Framework-Specific Notes

### Pandas (`02_Frameworks/01_Pandas/`)
- 73 lesson files covering dataframes, series, indexing, grouping, etc.
- 23 exercises
- README in Chinese
- Optional dependencies: openpyxl/xlsxwriter (Excel), pyarrow (Parquet), matplotlib (plotting)

### NumPy (`02_Frameworks/02_Numpy/`)
- 42 lesson files covering arrays, broadcasting, indexing, vectorization
- 14 exercises
- README in Chinese
- Focus on vectorized operations and performance

### Requests (`02_Frameworks/03_Requests/`)
- 27 lesson files (14 basic + 13 advanced)
- 12 exercises
- README in Chinese
- Basic: installation, GET/POST, response parsing, timeouts, Session/Cookie, redirects, streaming downloads, uploads, Basic Auth, retries
- Advanced: PUT/PATCH/DELETE/HEAD/OPTIONS, proxies, SSL verification, Digest Auth/Bearer Token/API Key, event hooks, connection pool, raw request body, URL encoding, Cookie persistence, Response.raw, DNS/connection reuse, AsyncIO integration
- Uses httpbin.org public API for demonstrations

## Important Notes

- **No build process**: Pure Python, direct execution only
- **No packaging**: Educational resource, not a library
- **Bilingual docs**: Respect existing Chinese READMEs for basics topics
- **Validation philosophy**: Run lessons to verify; don't break the runnable-everything approach
- **Python 3.11+ features**: Uses modern syntax (type hints, match statements, etc.)
- **main.py**: Minimal demo entry point; actual learning happens by running individual lesson files
- **Virtual environment**: Created at `.venv/` by `uv sync`; use `uv run` or activate manually
