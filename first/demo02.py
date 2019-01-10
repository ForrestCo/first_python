# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : demo02.py
# @Author: 杨崇
# @Date  : 2019/1/7
# @Desc  : 循环

# number_l = int(input("请输入number_l:"))
# number_r = int(input("请输入number_r:"))
# temp = number_l + number_r
# print("两者之和为:", temp)


# str1 = str(input("请输入姓名:"))
# int1 = int(input("请输入年龄:"))
# float1 = float(input("请输入身高:"))
#
# print("姓名:%s  年龄:%d   身高:%.02f" % (str1, int1, float1))


# company = str(input("公司名称:"))
# name = str(input("姓名:"))
# title = str(input("职位:"))
# number = int(input("电话:"))
# mail = str(input("邮箱:"))
# print("*" * 50)
# print(" " * 18, "公司名称: %s" % company)
# print(" ")
# print(" " * 18, "姓名: %s(%s)" % (name, title))
# print(" ")
# print(" " * 18, "电话: %d" % number)
# print(" " * 18, "e-mail: %s" % mail)
# print("*" * 50)

# 计算 0 ~ 100 之间所有数字的累计求和结果
# i = 0
# count1 = 0  # 总和
# while i <= 100:
#     count1 = count1 + i
#     i += 1
# print(count1)

# 计算 0 ~ 100 之间所有数字的累计求和结果
# j = 0
# count2 = 0  # 总和
# while j <= 100:
#     if j % 2 == 0:
#         count2 = count2 + j
#     j += 1
# print("0 ~ 100 之间所有数字的累计求和结果为:", count2)

# break 与 continue
# break:直接退出整个循环
# continue:退出本次循环
# k = 0
# l1 = 0
# while k <= 10:
#     while l1 == k + 1:
#         l1 += 1
#         print(l1)
#         break
#     print(k)
#     k += 1

# 在控制台连续输出五行 *，每一行星号的数量依次递增
i = 1
j = 13
result = 0

while i <= 13:
    result = j//2 - (i-1)
    print(result * ' ', '*' * i)
    i += 1

