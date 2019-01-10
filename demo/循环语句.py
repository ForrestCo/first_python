# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 循环语句.py
# @Author: 杨崇
# @Date  : 2018/11/9
# @Desc  : 循环语句

# Python循环语句
"""
    while 循环
    for 循环
    嵌套循环

循环控制语句:
    break；--在语句块执行过程中终止循环，并且跳出整个循环
    continue; --在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
    pass； --pass是空语句，是为了保持程序结构的完整性
"""

# Python while循环语句
"""
    while 判断条件：
        执行语句........ 
"""

count = 0
while count < 9:
    print("当前count的值为：",count)
    count += 1

print("循环结束!")


# break 和 continue关键字使用
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

# 无限循环
var = 1
# while var == 1:  # 该条件永远为true，循环将无限执行下去
#     num = raw_input("Enter a number  :")
#     print "You entered: ", num
#
# print "Good bye!"


# 循环语句中使用else
count = 0
while count <= 5:
    print("count小于5", count)
    count += 1
else:
    print("count大于5", count)


# for循环
tt = 10
pp = [1, 2]
if tt in pp:
    print("in")
else:
    print("not in")
# for tt in pp:
#     print "当前字母 :", tt
