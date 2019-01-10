# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 杨崇.py
# @Author: 杨崇
# @Date  : 2019/1/8
# @Desc  : null

# - 打印出100 以内的 2  和 5 的公倍数
i = 2
j = 5
k = 100
q = 0
li = []
while q <= 100:
    if q % i == 0 and q % j == 0:
        li.append(q)
    q += 1
print(li)

# - 判断101-200之间有多少个素数，并输出所有素数。
# 一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数
a = 101
b = 200
li1 = []
while a <= b:
    k = 2
    while k < a:
        if a % k == 0:
            break
        k += 1
    else:
        li1.append(a)
    a += 1
print('素数:', li1)
