# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 剪刀石头布.py
# @Author: 杨崇
# @Date  : 2019/1/6
# @Desc  : null

import random

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
k = 0
jx = 0   # 是否继续

# 定义用户赢得次数 count
count = 0
while k < 100:
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
            print("连续输错 %d 次" % i)
            if i == 3:
                print("连续输错 %d 次,直接退出" % i)
                break
        j += 1
        jx = str(input("有种接着来呀！！！ (Y / N):"))
        if jx == "Y":
            ren = str(input("请出手:"))
            break
        elif jx == "N":
            print("怕了吗？胆小鬼！！！！！哈哈哈~~~~")
            break
        else:
            print("您的输入有误！！！  游戏到此结束！！！")
            break
    k += 1
