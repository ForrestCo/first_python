# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 循环.py
# @Author: 杨崇
# @Date  : 2019/1/7
# @Desc  : null

# i = 0
# while i < 5:
#     print("输出:%d次" % (i + 1))
#     i += 1
# print('i的值为:', i)

# *字塔
i = 1
# j=1
while i <= 9:
    if i <= 5:
        print("*" * i)

    elif i <= 9:
        j = i - 2 * (i - 5)
        print("*" * j)
    i += 1
else:
    print("")

i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j): break
        j = j + 1
    if j > i / j:
        print
    i, " 是素数"
    i = i + 1

print
"Good bye!"
