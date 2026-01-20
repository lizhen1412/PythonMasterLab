# Repository Guidelines

## Project Structure & Module Organization
- `01_Basics/` core lessons grouped by numbered topic folders (e.g., `01_Basics/02_Variables/`).
- Each topic includes `README.md`, a runnable `01_overview.py`, numbered lessons `NN_description.py`, and an `Exercises/` subfolder.
- `02_Frameworks/` framework notes; currently `01_Pandas/` and `02_Numpy/` mirror the same lesson/exercise layout.
- `docs/` reserved for future documentation; `main.py` is a lightweight entry script.

## Environment & Dependencies
- Python 3.11+ is required.
- Optional libraries are used by framework lessons: `numpy>=2.4.0`, `pandas>=2.3.3`.
- Install only what you need: `python3 -m pip install numpy pandas`.

## Build, Test, and Development Commands
- Run a topic index: `python3 01_Basics/02_Variables/01_overview.py`.
- Run a single lesson: `python3 01_Basics/02_Variables/02_variable_basics.py`.
- Syntax check the basics track: `python3 -m compileall 01_Basics`.

## Coding Style & Naming Conventions
- Use 4-space indentation and standard Python 3.11 syntax.
- Follow `snake_case` for functions and files.
- Keep lesson ordering with numeric prefixes (`01_`, `02_`, ...) and keep `01_overview.py` as the entry point per topic.
- Keep examples runnable and self-contained; avoid hidden dependencies across lessons.

## Testing Guidelines
- There is no dedicated test suite today.
- For validation, prefer running the lesson directly or use `python3 -m compileall`.
- If you add tests, place them under `tests/` and name files `test_*.py`; use stdlib `unittest` unless you introduce a new framework.

## Commit & Pull Request Guidelines
- The repository has no commit history yet, so no established convention exists.
- Use short, imperative subjects (e.g., `Add numpy indexing exercises`, `Fix variable scoping example`).
- PRs should include: a short summary, affected topic paths (e.g., `01_Basics/11_Loops/`), and the command(s) you ran to validate changes.
