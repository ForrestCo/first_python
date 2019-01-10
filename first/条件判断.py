# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 条件判断.py
# @Author: 杨崇
# @Date  : 2019/1/7
# @Desc  : null

# bool1 = False
#
# if bool1:
#     print(bool1)
# else:
#     print(bool1)
#
#
# age = 17
# if age == 18:
#     print("欢迎光临!!!")
# else:
#     print("未成年不得入内!!!")

# 从键盘输入一个数判断是否为偶数
i = int(input("请输入一个整数:"))
if i % 2 == 0:
    print("是")
else:
    print("不是")

# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
#
#    要求人的年龄在 0-120 之间
# age = int(input("请输入年龄:"))
# i = 0
# while i < 10:
#     if 0 <= age <= 120:
#         print("你的年龄是:%s" % age)
#         break
#     else:
#         age = int(input("你是人是鬼,请重新输入:"))
#     i += 1

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
#
#     要求只要有一门成绩 > 60 分就算合格
# python_score = float(input("请输入Python成绩:"))
# c_score = float(input("请输入C成绩:"))
#
# if python_score > 60 or c_score > 60:
# #     print("及格")
# # else:
# #     print("不及格")

# i = 1
# j = i
# j += 1
# j -= 1
# j *= 2
# j /= 2
# print(j)

#
#     定义 holiday_name 字符串变量记录节日名称
#     如果是 情人节 应该 买玫瑰／看电影
#     如果是 平安夜 应该 买苹果／吃大餐
#     如果是 生日 应该 买蛋糕
#     其他的日子每天都是节日啊……
# holiday_name = "平安夜"
# if holiday_name == "情人节":
#     print("买玫瑰／看电影")
# elif holiday_name == "平安夜":
#     print("买苹果／吃大餐")
# elif holiday_name == "生日":
#     print("买蛋糕")
# else:
#     print("其他的日子每天都是节日啊……")

# f = 3.14
# i = int(f)
# print(i)

# has_ticket = True
# knife_length = 21
# if has_ticket:
#     print("验票通过,请过安检!")
#     if knife_length >= 20:
#         print('安检未通过!')
#     else:
#         print('安检通过!')
# else:
#     print('请先购买车票!')
#
# #  对a b c 进行排序
# a, b, c = 8, 2, 10
# if a > b:
#     if b > c:
#         print("a > b > c")
#     else:
#         print("a > c > b")
# elif a > c:
#     if c > b:
#         print("a > c > b")
#     else:
#         print("a > b > c")
# elif b > c:
#     if c > a:
#         print("b > c > a")
#     else:
#         print("b > a > c")

# 定义一个列表
# li = [4, 5, 6, 7, 3, 2, 6, 9, 8]
# count = len(li)
# for q in count(0, count):
#     print(li[q])


