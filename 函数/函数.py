# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 函数.py
# @Author: 杨崇
# @Date  : 2019/1/10
# @Desc  : 函数

# 定义一个函数


# def say_hello():
#     print("hello 1")
#     print("hello 2")
#     print("hello 3")
#
# say_hello

#
# def my_def(a, b):
#     """
#     :param a:
#     :param b:
#     :return:
#     """
#     count = a + b
#     return count
#
# # CTRL + Q
# print(my_def(1, 2))


# a = 5
#
#
# def test1(a):
#     a += 1
#     print("%d" % a)
#
# test1(2)
# print("%d" % a)

# 写一个函数求三个数的和


# def demo(a, b, c):
#     count = a + b + c
#     return count
#
# result = demo(1, 2, 3)
# print(result)
#
# # 写一个函数求三个数的平均值
#
#
# def demo2(a, b, c):
#     avg = (a + b + c) / 3
#     return avg
# result = demo2(1, 2, 3)
# print(result)


# a = 10
#
#
# def test():
#     a = 5
#     print("函数内a：%d" % a)
#
# test()
# print("函数外a：%d" % a)


# a = 10
#
#
# def test():
#     global a
#     a = 5  # 修改全局变量
#     print("函数内a：%d" % a)
#
# test()
# print("函数外a：%d" % a)


# def printinfo(name, age = 35):
#    # 打印任何传入的字符串
#    print("Name: %s", % name)
#    print("Age: %s", % age)
#
# # 调用printinfo函数
# printinfo("miki")
# printinfo("miki", 20)


f = open('test.txt', 'w')
f.write('hello world, i am here!')
f.close()

f = open('test.txt', 'r')

content = f.read(5)

print(content)

print("-"*30)

content = f.read()

print(content)

f.close()





