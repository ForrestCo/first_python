# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : dd.py
# @Author: 杨崇
# @Date  : 2019/1/6
# @Desc  : null
#
# name = "小明"
# age = None
# sex = "男"
# height = 180.5
# weight = 75.5
# isDetele = True
# print(name, age, sex, height, weight)
#
# print(type(name))
# print(type(isDetele))
# print(type(height))
# print(type(age))
# result = type(height)
# print(result)

# 运算符
import random
import time

"""
a = 10
b = 3
# 相加
result = a + b
print(result)

# 相减
result = a - b
print(result)

# 相乘
print(a * b)

# 除
print(a / b)

# 取余
print(a % b)

# 取整
print(a // b)

# 乘方
print(a ** b)

# 运算符优先级
print(a - a * b)

# 字符串拼接
str1 = "abc"
str2 = "def"
print(str1 + str2)

# 字符串和整型相乘，输出s个字符串的拼接
str1 = "*"
s = 50
print(str1 * s)

# 字符串和数字相乘类型还是字符型
print(type(str1 * s))

# username = str(input("请输入用户名："))
# password = str(input("请输入密码："))
# print("用户名为：%s, 密码为：%s" % (username, password))
#
# format_str = "用户名为：%s,密码为：%s"

print('*' * 50)

# 输出 我的名字叫 小明，请多多关照！
name = "小明"
print("我的名字叫%s，请都多关照" % name)

# 输出 我的学号是 000001
id = 1
print("我的学号是:%06d" % id)
# 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00
a = 9
b = 5
c = 45
print("苹果单价:%.02f元/斤,购买了:%.02f 斤，需要支付:%.02f" % (a, b, c))

# 输出 数据比例是 10.00%
s = 10
print("数据比例是:%.02f%%" % s)

"""

# 石头剪刀布
# 电脑生成1~3的随机数
computer = random.randint(1, 3)

# 对computer重新赋值
if computer == 1:
    computer = "石头"
elif computer == 2:
    computer = "剪刀"
else:
    computer = "布"

# 人输入
ren = str(input("请出手:"))

# 对人的输入做验证,如果人输入的不是（剪刀，石头，布）则提示 “您的输入有误，请重新输入....”
# 用户输错3次直接退出程序
i = 0  # 用户输错次数
j = 0  # 连续玩的次数
jx = 0   # 是否继续

# 定义用户赢得次数 count
count = 0
while j < 100:
    while i < 3:
        if ren == "石头" or ren == "剪刀" or ren == "布":
            if ren == "石头" and computer == "剪刀" or \
                    ren == "剪刀" and computer == "布" or \
                    ren == "布" and computer == "石头":
                print("电脑：", computer)
                print("恭喜你赢了！！！")
                break
            elif ren == computer:  # 平手的情况
                print("电脑：", computer)
                print("平局，有种再来呀！！！")
                break
            else:               # 输的情况
                print("电脑：", computer)
                print("死吧，虫子！！！")
                break
        else:
            ren = str(input("您的输入有误，请重新输入...:"))
            i += 1
            print("连续输错 %d 次!!!" % i)
            if i == 3:
                print("连续输错 %d 次,游戏结束!!!" % i)
    j += 1
    jx = str(input("有种接着来呀！！！ (Y / N):"))
    if jx == "Y":
        ren = str(input("请出手:"))
        continue
    elif jx == "N":
        print("怕了吗？胆小鬼！！！！！哈哈哈~~~~")
        break
    else:
        print("您的输入有误！！！  游戏到此结束！！！")
        break

