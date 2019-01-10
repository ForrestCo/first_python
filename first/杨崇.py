# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 杨崇.py
# @Author: 杨崇
# @Date  : 2019/1/7
# @Desc  : null
import random

# 手动输入一个数字，计算机随机生成一个数字，两个数字求和，判断这个数字的奇偶性
# 输入
number = int(input("请输入一个数字:"))

# 电脑随机生成
computer = random.randint(0, 10)
print('电脑:%d' % computer)
# 两数之和
count = number + computer
print('和:%d' % count)
# 判断奇偶性
if count % 2 == 0:
    print('为偶数')
else:
    print('为奇数')

