# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 函数.py
# @Author: 杨崇
# @Date  : 2018/11/10
# @Desc  : 函数

"""

    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。


"""


def function_name(str):
    print(str)


# 函数调用
function_name("简单的函数")


# 参数传递
"""
    在Python中，类型属于对象，变量没有类型的：
    a=[1, 2, 3]
    a="Runoob"
    在上面代码中，[1,2,3]是list类型,Runoob是String类型
    而变量a是没有类型，仅仅是一个对象的引用，可
    以是List类型对象
    也可以指向String类型对象
"""
