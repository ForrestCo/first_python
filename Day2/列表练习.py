# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 列表练习.py
# @Author: 杨崇
# @Date  : 2019/1/10
# @Desc  : null

import random

# my_list = ["zhangsan", "lisi", "wangwu", "lisi"]
# # 通过del 删除wangwu
# del my_list[2]
# print(my_list)

# 通过循环 删除lisi
# count = len(my_list)
# for j in range(0, count):
#     print(my_list[j])
#     if my_list[j] == 'lisi':
#         del my_list[j]
# print(my_list)
# 清空列表


# my_list = [1, 2, 3, 4, 5]
# li = []
# # count = len(my_list)
# # print(count)
# j = 4
# while j >= 0:
#     li.append(my_list[j])
#     j -= 1
# print(li)

# my_list = [1, 2, 3, 4, 5]
# count = len(my_list)
# for i in range(0, count):
#     temp = my_list.pop()
#     my_list.insert(i, temp)
# print(my_list)
#
# # index   count
# my_list = [1, 2, 3, 4, 5, 1]
# result = my_list.index(1)
# print(result)
# print(result)
# result1 = my_list.count(1)
# print(result1)


# list1 = [3, 9, 5, 2, 7, 4]
# count = len(list1)
# for i in range(0, count):
#     for j in range(1, count):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1)

# li = [3, 9, 5]
# count = len(li)
# for i in range(0, count):
#     for j in range(i + 1, count):
#         if li[i] > li[j]:
#             li[i], li[j] = li[j], li[i]
# print(li)

#
# names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# # 获取元素个数
# count = len(names)
# i = 0
# # while i < 10:
# #     # 生成随机数
# #     ran = random.randint(0, count)
# #     print(names[ran])
# #     i += 1
#
# for _ in range(0, 10):
#     # 生成随机数
#     ran = random.randint(0, count)
#     print(names[ran])


# li = [
#     [], [], []
# ]
# li1 = []
# count = len(li)
# print(count)
# names = ['jack', 'tom', 'rose']
# for i in range(0, count):
#     li[i].append(names[i])
# print(li)


# 一个学校，有3个办公室，
# 现在有8位老师等待工位的分配，请编写程序:
# 1> 完成随机的分配
# 2> 获取办公室信息 (每个办公室中的人数，及分别是谁)
school = [[], [], []]  # 定义学校和办公室
teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 定义教师信息

count_teacher = len(teacher)  # 获取teacher列表中的元素个数
count_school = len(school)   # 获取school列表中的元素个数

# 遍历teacher列表中的元素,追加到school[]中
for i in range(0, count_teacher):
    # 获取随机数
    result1 = random.randint(0, count_school-1)
    school[result1].append(teacher[i])
print(school)
for j in range(0, count_school):
    li1 = school[j]
    count3 = len(li1)
    for k in range(0, count3):
        print(li1[k], ' ', end='')
    print('')

# 列表嵌套
# li = [
#     ['河南', '郑州'],
#     ['浙江', '杭州'],
#     ['四川', '成都']
# ]
#
# count1 = len(li)
# for i in range(0, count1):
#     li1 = li[i]
#     count2 = len(li1)
#     for j in range(0, count2):
#         print(li1[j], '  ', end='')
#     print('')








