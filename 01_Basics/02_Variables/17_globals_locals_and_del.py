#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例 17：globals()/locals() 与 del（删除“名字绑定”）。

你会学到：
1) `globals()`：当前模块的全局名字表（dict）
2) `locals()`：当前作用域的局部名字表（dict）
3) `del name` 删除的是“名字绑定”，不是“强制删除对象”
   - 如果还有其它引用，对象仍然存在

运行：
    python3 01_Basics/02_Variables/17_globals_locals_and_del.py
"""


def main() -> None:
    print("1) globals()/locals()：")
    module_var = "I am local to main()"
    print("'__name__' in globals() ->", "__name__" in globals())
    print("'module_var' in globals() ->", "module_var" in globals())
    print("'module_var' in locals()  ->", "module_var" in locals())

    print("\n2) del 删除的是名字：")
    value = [1, 2]
    alias = value
    print("before del: value =", value, "| alias =", alias, "| value is alias =", value is alias)
    del value
    print("after del: alias still works ->", alias)
    alias.append(3)
    print("after alias.append(3): alias =", alias)

    print("\n3) del 也可以作用在容器元素上：")
    numbers = [0, 1, 2, 3, 4]
    print("before:", numbers)
    del numbers[1]
    del numbers[2:4]
    print("after :", numbers)

    data = {"a": 1, "b": 2}
    print("\nbefore:", data)
    del data["a"]
    print("after :", data)


if __name__ == "__main__":
    main()

