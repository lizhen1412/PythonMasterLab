# Repository Guidelines

## Project Structure & Module Organization
- `01_Basics/` core lessons grouped by numbered topic folders (e.g., `01_Basics/02_Variables/`).
- Topics generally include `README.md`, a runnable `01_overview.py`, and numbered lessons `NN_description.py`.
- Exercises are organized in two patterns: early centralized tracks under `01_Basics/08_Exercises/`, and chapter-local `Exercises/` subfolders in many later topics.
- `02_Frameworks/` framework notes; currently `01_Pandas/`, `02_Numpy/`, `03_Requests/`, and `04_Playwright/` mirror the lesson/exercise layout.
- `docs/` reserved for future documentation; `main.py` is a lightweight entry script.

## Environment & Dependencies
- Python 3.11+ is required, and the repo is pinned via `.python-version` (`3.11`).
- Prefer `python3.11` (or `uv run python`) in commands to avoid interpreter mismatch on systems where `python3` points to older versions.
- Core framework dependencies: `numpy>=2.4.0`, `pandas>=2.3.3`, `requests>=2.32.3`, `playwright==1.58.0`.
- Optional dependencies used by advanced examples: `matplotlib`, `pyarrow`/`fastparquet`, `tables`, `lxml`/`beautifulsoup4`, `scipy`, `openpyxl`/`xlsxwriter`.
- Install only what you need:
  - Core: `python3.11 -m pip install numpy pandas requests playwright==1.58.0`
  - Playwright browsers: `python3.11 -m playwright install`
  - Optional (as needed by specific lessons): `python3.11 -m pip install matplotlib pyarrow lxml scipy tables openpyxl xlsxwriter`

## Build, Test, and Development Commands
- Run a topic index: `python3.11 01_Basics/02_Variables/01_overview.py`.
- Run a single lesson: `python3.11 01_Basics/02_Variables/02_variable_basics.py`.
- Syntax check all learning tracks:
  - `PYTHONPYCACHEPREFIX=/tmp/pycache python3.11 -m compileall 01_Basics 02_Frameworks`
- For faster local checks on touched areas, compile only changed folders/files.

## Coding Style & Naming Conventions
- Use 4-space indentation and standard Python 3.11 syntax.
- Follow `snake_case` for functions and files.
- Keep lesson ordering with numeric prefixes (`01_`, `02_`, ...) and keep `01_overview.py` as the entry point per topic.
- Keep examples runnable and self-contained; avoid hidden dependencies across lessons.

## Testing Guidelines
- There is no dedicated test suite today.
- For validation, prefer running the lesson directly or use compile checks with Python 3.11.
- Requests chapter examples rely on external network access (httpbin). If offline, validate syntax and run non-network examples first.
- If you add tests, place them under `tests/` and name files `test_*.py`; use stdlib `unittest` unless you introduce a new framework.

## Commit & Pull Request Guidelines
- Use short, imperative subjects (e.g., `Add numpy indexing exercises`, `Fix variable scoping example`).
- PRs should include: a short summary, affected topic paths (e.g., `01_Basics/11_Loops/`), and the command(s) you ran to validate changes.
- Keep `AGENTS.md`, root `README.md`, and `pyproject.toml` dependency/runtime notes consistent when environment or module layout changes.
