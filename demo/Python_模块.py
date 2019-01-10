# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : Python_模块.py
# @Author: 杨崇
# @Date  : 2018/11/10
# @Desc  : 模块

# 模块引入
from demo import support

# 调用模块中的方法
support.print_func("yc")

# from...import
# from语句让你从模块中导入一个指定的
# 部分到当前命名空间中

# from fib import fibonacci
# 这个声明不会把整个 fib 模块导入到当前的命名空间中，
# 它只会将 fib 里的 fibonacci
# 单个引入到执行这个声明的模块的全局符号表。


