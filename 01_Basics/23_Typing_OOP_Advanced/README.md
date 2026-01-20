# Python 3.11+ Typing and OOP Advanced (Chapter 23)

This chapter focuses on advanced type hints and object-oriented patterns:
- typing basics beyond the intro (Union/Optional/Literal)
- generics with TypeVar and Protocol
- TypedDict and NewType
- ParamSpec, TypeGuard, Self
- future annotations and get_type_hints
- abc and abstract methods
- MRO and cooperative super()
- advanced dataclass options

---

## 1) How to run

From repo root:

- Index: `python3 01_Basics/23_Typing_OOP_Advanced/01_overview.py`
- Single lesson: `python3 01_Basics/23_Typing_OOP_Advanced/06_typing_callable_paramspec.py`
- Exercises index: `python3 01_Basics/23_Typing_OOP_Advanced/Exercises/01_overview.py`

---

## 2) Key topics checklist

- Union/Optional/Literal for precise APIs
- Generic functions/classes with TypeVar
- Protocol for structural typing
- TypedDict for dict-shaped data
- NewType for stronger semantic types
- ParamSpec to preserve decorator signatures
- TypeGuard for type narrowing
- Self for fluent methods
- __future__ annotations and forward refs
- abc.ABC and @abstractmethod
- MRO and super() in multiple inheritance
- dataclass advanced options: frozen/slots/order/field

---

## 3) Files

| No. | File | What it covers |
|---:|---|---|
| 01 | [`01_overview.py`](01_overview.py) | Index of lessons |
| 02 | [`02_typing_unions_optional_literal.py`](02_typing_unions_optional_literal.py) | Union/Optional/Literal basics |
| 03 | [`03_typing_typevar_generics.py`](03_typing_typevar_generics.py) | TypeVar and generics |
| 04 | [`04_typing_protocols_structural.py`](04_typing_protocols_structural.py) | Protocol and structural typing |
| 05 | [`05_typing_typeddict_newtype.py`](05_typing_typeddict_newtype.py) | TypedDict and NewType |
| 06 | [`06_typing_callable_paramspec.py`](06_typing_callable_paramspec.py) | Callable and ParamSpec |
| 07 | [`07_typing_typeguard_self.py`](07_typing_typeguard_self.py) | TypeGuard and Self |
| 08 | [`08_future_annotations_and_get_type_hints.py`](08_future_annotations_and_get_type_hints.py) | __future__ annotations and get_type_hints |
| 09 | [`09_abc_and_abstractmethod.py`](09_abc_and_abstractmethod.py) | abc and abstract methods |
| 10 | [`10_mro_and_super.py`](10_mro_and_super.py) | MRO and cooperative super() |
| 11 | [`11_dataclass_advanced.py`](11_dataclass_advanced.py) | dataclass advanced options |
| 12 | [`12_chapter_summary.py`](12_chapter_summary.py) | Summary |
| 13 | [`Exercises/01_overview.py`](Exercises/01_overview.py) | Exercises index |

---

## 4) Exercises

Run: `python3 01_Basics/23_Typing_OOP_Advanced/Exercises/01_overview.py`

- `Exercises/02_parse_int_optional.py`: Optional return for parsing
- `Exercises/03_generic_first_or.py`: TypeVar-based generic helper
- `Exercises/04_protocol_total_size.py`: Protocol + __len__
- `Exercises/05_typeddict_format_user.py`: TypedDict with optional field
- `Exercises/06_typeguard_str_list.py`: TypeGuard for list[str]
- `Exercises/07_dataclass_frozen_point.py`: Frozen dataclass point
