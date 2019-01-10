# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : IO.py
# @Author: 杨崇
# @Date  : 2018/11/10
# @Desc  : 文件/IO

# 读取键盘输入
"""
    Python提供了两个内置函数从标准输入读入一行文本，默认的输入是键盘
    raw_input
    input

"""

# raw_input函数,raw_input([prompt]),从标准输入读取一个行，并返回一个字符串
# str = raw_input("请输入：")
# print "您输入的内容是：", str

# input函数,input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，
# 但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
str = input("请输入：")
print("您输入的内容是：", str)
# 打开和关闭文件

# open函数,使用open函数打开一个文件，
# 创建一个file对象，相关的方法才可以调用它进行读写
# 语法：

