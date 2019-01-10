# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 列表.py
# @Author: 杨崇
# @Date  : 2019/1/7
# @Desc  : list

# 文件重命名    shift + F6

# li = []  # 定义一个空列表
# li.append(1)
# print(li[0])

# li1 = [1, 3, 5, 8, 6, 2]
# # 降序
# li1.sort(reverse=True)
# print(li1)
#
# # 升序
# li1.sort(reverse=False)
# print(li1)


i = 0
li = []  # 用来存多条菜品信息
li2 = []  # 用来存单价
zj = 0  # 总价
count1 = 0
jx = 0
while i < 2:
    name = str(input("菜品的名称:"))
    price = int(input("单价:"))
    number = int(input("数量:"))
    tu = (name, price, number)
    zj = zj + price * number  # 总价 = 单价 * 数量
    li.append(tu)  # 把每条菜品信息添加到列表中
    jx = str(input("下一道(X)   完成(Y) : "))
    if jx == 'X':
        continue
    elif jx == 'Y':
        break
    else:
        print('输入有误,请重新输入:')
print(li)
print('')
print('欢迎来到XX饭馆')
print('您购买的商品清单如下')
print('*' * 30)
count = len(li)  # 获取列表的长度
for i in range(0, count):
    dc = li[i]
    count2 = len(dc)
    print()
    for j in range(0, count2):
        print(dc[j], '   ', end='')
print('\n')
print('*' * 30)
print('总价格为：%.02f 元' % zj)



# 冒泡排序
# temp = 0
# li = [6, 3, 4, 100, 8, 5, 40, 31]
# count = len(li)
# for i in range(0, count):
#     for j in range(i + 1, count):
#         if li[i] > li[j]:
#             li[i], li[j] = li[j], li[i]
# print(li)

# 快速排序




