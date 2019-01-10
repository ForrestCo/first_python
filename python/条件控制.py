# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 条件控制.py
# @Author: 杨崇
# @Date  : 2019/1/5
# @Desc  : 条件控制
import random

# 输入年龄
# x = 5
# y = 5
# print(x == y)
#
# i = 32
# if 0 < i < 10:
#     print('0<i<10')
# elif 10 < i < 20:
#     print('10< i <20')
# elif 20 < i < 30:
#     print('20< i <30')
# elif 30 < i < 40:
#     print('30< i <40')

# 剪刀：1 石头：2 布：3
# i = int(input('请输入:'))
# 随机数
# computer = random.randint(1, 3)
# # print(computer)
# if i == 1 and computer == 3 or i == 2 and computer == 1 or i == 3 and computer == 2:
#     print('你赢了！')
# elif i == computer:
#     print('平局')
# else:
#     print('你输了')

# 计算 0 ~ 100 之间所有数字的累计求和结果
i = 0
sum1 = 0
while i <= 100:
    sum1 = sum1 + i
    i += 1
print('0~100累计和：', sum1)

# 计算 0 ~ 100 之间 所有 偶数 的累计求和结果
# 偶数
i = 6
sum2 = 0
while i <= 100:
    if i % 2 == 0:
        sum2 = sum2 + i
    i += 1
print(sum2)

# i = 0
#
# while i < 10:
#
#     # break 某一条件满足时，退出循环，不再执行后续重复的代码
#     # i == 3
#     if i == 3:
#         break
#
#     print(i)
#
#     i += 1
#
# print("over")

# i = 0
#
# while i < 10:
#
#     # 当 i == 7 时，不希望执行需要重复执行的代码
#     if i == 7:
#         # 在使用 continue 之前，同样应该修改计数器
#         # 否则会出现死循环
#         print(i)
#         i += 1
#         print(i)
#         break
#
#     # 重复执行的代码
#     # print(i)
#
#     i += 1
#     print(i)i = 0
#
# while i < 10:
#
#     # 当 i == 7 时，不希望执行需要重复执行的代码
#     if i == 7:
#         # 在使用 continue 之前，同样应该修改计数器
#         # 否则会出现死循环
#         print(i)
#         i += 1
#         print(i)
#         break
#
#     # 重复执行的代码
#     # print(i)
#
#     i += 1
#     print(i)


# 九九乘法表
# i = 1
# while i <= 9:
#     while i <= i+1:
#         print(i, '*', i)
#         i += 1
#         break
#     i += 1
