# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 变量.py
# @Author: 杨崇
# @Date  : 2019/1/3
# @Desc  : null


# 定义一个字符串
str1 = 'abcdefg'
str2 = '123456'

# 输出第一个字符
print('第一个字符:', str1[0])

# 输出字符串中第一个到第五个之间的字符串
print('第一个到第四个字符：', str1[0:4])

# 输出从第三个字符串开始的字符串
print('第三个字符开始的字符', str1[2:])

# 输出字符串2次
print('输出字符串2次', str1 * 2)

# 输出拼接字符串
print('字符串拼接', str1 + str2)

'''
Python五个标准数据类型：
        Numbers(数字)、
        String（字符串）、
        List（列表）、
        Tuple(元祖)、
        Dictionary(字典)
'''
# 定义一个列表
li = ['yc', 123, 'a', 'b', 'c', 'd']
li1 = [1, 2, 3, 4]

# 输出列表中的元素
print('列表li中的元素：', li)

# 输出li中第二个元素
print('li中的第二个元素：', li[1])

# 输出列表中第一个到第二个元素
print('输出第一个到第三个元素：', li[0:3])

# 输出第三个开始至列表末尾的所有元素
print('输出第三个至末尾的所有元素：', li[2:])

# 输出列表两次
print('输出列表2次：', li * 2)

# 打印组合的列表
print('组合列表', li + li1)

# python 元组
'''
    元祖类似于列表，元祖用 “（）”标识，内部元素用逗号隔开，
    相当于只读列表。

'''

# 定义一个元祖
y = ('yc', 123, 'a', 'b', 'c', 'd', 11, 'string')

# 输出元组
print('输出元组y：', y)

# 输出元组中第三个元素
print('输出元组中第三个元素：', y[2])


# 字典
'''
   字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
   列表是有序的对象集合，字典是无序的对象集合。 
   两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
   字典用"{ }"标识。字典由索引(key)和它对应的值value组成。 
'''

# 定义一个字典
dic = {'name': 'admin', 'password': '123456'}
print('输出字典dic:', dic)

# 输出name
print('输出name的值：', dic['name'])

# 输出所有的键
print('输出所有的键：', dic.keys())

# Sets集合
"""
    无序的不重复元素的集合
    可以消除重复的元素
    创建一个空集合set()
    set{}是用来创建一个空字典
"""
# 创建一个set集合
users = {'a', 'a', 'b', 'c', 'd', 'd'}
print('输出集合users中的元素：', users)

# 对set集合进行运算
a = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
b = {'a', 'a', 'f', 'a', 'h', 'n'}

print('集合a:', a)
print('集合b:', b)

# a和b的差集
print('a和b的差集：', a - b)

# a和b的并集
print('a和b的并集：', a | b)

# a和b的交集
print('a和b的交集：', a & b)

# a和b中不同时存在的元素
print(a ^ b)



# python 循环
"""
    while 循环
    for 循环
    嵌套循环

循环控制语句:
    break；--在语句块执行过程中终止循环，并且跳出整个循环
    continue; --在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
    pass； --pass是空语句，是为了保持程序结构的完整性
"""

# count = 0
# while count < 9:
#     print("当前count的值为：", count)
#     count += 1
#
# print("循环结束!")





