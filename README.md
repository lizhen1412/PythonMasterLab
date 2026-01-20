PythonMasterLab
===============

This repository contains runnable, topic-based Python lessons.
Each topic lives under `01_Basics/` with a `README.md` and a runnable
`01_overview.py` index. Framework notes live under `02_Frameworks/`.

Quick start
-----------

- Run a topic index:
  `python3 01_Basics/02_Variables/01_overview.py`
- Run a single lesson:
  `python3 01_Basics/02_Variables/02_variable_basics.py`
- Compile check (basics):
  `python3 -m compileall 01_Basics`

Structure
---------

- `01_Basics/`: core Python lessons by topic
- `02_Frameworks/`: framework notes（Pandas、NumPy、Requests）
- `docs/`: placeholder for future docs

Requirements
------------

- Python 3.11+
- Optional: `numpy>=2.4.0` for `02_Frameworks/02_Numpy`
- Optional: `pandas>=2.3.3` for `02_Frameworks/01_Pandas`
