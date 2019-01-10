# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 循环.py
# @Author: 杨崇
# @Date  : 2019/1/7
# @Desc  : null

# 定义一个列表
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in li:
#     print(i)
#
# t = len(li)
# for i in range(0, t):

# name = str(input("请输入菜名:"))
# price = str(input("请输入单价:"))
# number = str(input("请输入数量:"))
#
# print('欢迎来到XX饭馆')
# print('您购买的商品清单如下')
# print(name, price, number)
#
#
# i = 0
# while i < 10:
#     name = str(input("请输入菜名:"))
#     price = str(input("请输入单价:"))
#     number = str(input("请输入数量:"))

# li = []
# count = len(li)
# user = str(input("请输入:"))
# for i in range(0, count):
#     li.append(user)
#     print(li[1])

# 0 ~ 100所有数的和
"""
i = 0
count = 0  # 总和
while i <= 100:
    count = count + i
    i += 1
print('0 ~ 100所有数的和为:', count)


# 0~10之间的偶数和
j = 0
count2 = 0  # 总和
while j <= 10:
    if j % 2 == 0:
        count2 = count2 + j
    j += 1
print('0~10之间的偶数和为:', count2)


# 0~n之间的奇数和
k = 0
n = int(input("请输入一个数:"))
count3 = 0
while k <= n:
    if i % 2 != 0:
        count3 = count3 + k
    k += 1
print('0~%d之间的奇数和为:%d' % (n, count3))
"""
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# j = 1
# while j <= 5:
#     print('*' * j)
#     j += 1
#     if j == 5:
#         while j >= 0:
#             print('*' * j)
#             j -= 1
#         break

"""
i = 1
while i <= 5:
    print((5 - i) * ' ', (2 * i - 1) * '*')
    i += 1

j = 4
while j >= 0:
    print((5 - j) * ' ', (2 * j - 1) * '*')
    j -= 1


str1 = 'p'
print(str1 * 0)

"""

# i = 0
# while i < 5:
#     print("aaaaaaaaaa")
#     j = 0
#     while j < 5:
#         print("bbbbbbbbbbbbbbb", end="")
#         j += 1
#     i += 1

# j = 1
# while j <= 5:
#     i = 1
#     while i <= j:
#         print("*", end='')
#         i += 1
#         print()
#     j += 1

# j = 1
# while j <= 9:
#
#     i = 1
#     while i <= j:
#         print("*", end="")
#         i += 1
#     # 打印一排星星之后需要换行,在打印下一排
#     print("")
#
#     j += 1


"""
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print(b, '*', a, '=', a * b, ' ', end='')
        b += 1
    print('')
    print('')
    a += 1
"""

# print("Hello /World/")
# print("Hello /'World/'")
# # print("Hello /World/")
# # print("Hello /World/")
# # print("Hello /World/")
# # print("Hello /World/")

i = 0
j = 0
b = True
while i < 5:
    if not b:
        break
    while j < 5:
        j += 1
        print("第一层")
        if j == 1:
            b = False
        break
    i += 1
    print("第二层")






