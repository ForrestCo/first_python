# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 列表.py
# @Author: 杨崇
# @Date  : 2019/1/8
# @Desc  : null

# 定义一个空列表
# li = []
#
# li1 = [1, '张三', 'jack', 'Rose']
# print(li1)
# print(li)
#
# count = len(li1)
# count1 = len(li)
# print(count)
# print(count1)

import keyword

# li = []   # 定义一个空的列表
# li1 = [1, 3, 'jack', 'Rose']
#
# # 添加元素
# # 在末尾追加数据    列表.append(数据)
# li1.append('张三')
#
# # 在指定位置插入数据(位置前有空元素会补位)     列表.insert(索引, 数据)
# li1.insert(1, '李四')
# li.insert(2, 'jack')
# print(li1)
# print(li1[1])
# print(len(li))
# print(li[0])
#
# # 将可迭代对象中 的元素 追加到列表     列表.extend(Iterable)
# li2 = [1, 2, 3, '李四']
# li.extend(li2)
# print('remove删除:', li)
#
# # 删除元素
# #  	删除指定索引的数据 ,直接从内存中删除    del 列表[索引]
# del li[0]
# print(li)
#
# 删除第一个出现的指定数据  ------ 列表.remove(数据)
# li = [1, 2, 'jack', 4, 'jack']
# li.remove('jack')
# print(li)
#
# #  	删除末尾数据,返回被删除的元素     列表.pop()
# print(li.pop())
# print(li)
#
# # 删除指定索引数据------ 列表.pop(索引)
# li = [1, 2, 'jack', 4, 'jack']
# i = li.pop()
# print(i)
# print(li)

# # 清空列表-----     列表.clear
# li.clear()
# print(li)
#
#
# # 修改元素------    列表[索引] = 数据
# li = [1, 2, 3, 4, 'jack', 'Rose']
# li[1] = 'yc'
# print(li)
#
#
# # 查看    列表[索引]
#
# # 根据值查询索引，返回首次出现时的索引，没有查到会报错
# # 数据在列表中出现的次数
# # 列表.count(数据)
# print(li.index('yc'))
#
#
# # 数据在列表中出现的次数
# print(li.count(1))
#
# # 列表长度
# print(len(li))
#
# # 检查列表中是否包含某元素
# # if 数据 in 列表:
# if 'y' in li:
#     print("true")
# else:
#     print("false")
#
# # 排序
# #  	升序排序    列表.sort()
# li.clear()
# li = [6, 5, 7, 9, 3, 1, 3]
# print(li)   # 排序前
# # li.sort()
# print(li)   # 排序后
#
# # 降序排序
# # 列表.sort(reverse=True)
# li.sort(reverse=True)    # 降序排序  reverse = True
# li.sort(reverse=False)   # 升序排序  reverse = False
# print(li)
# print("*" * 50)
# # 逆序、反转    	列表.reverse()
# li = [6, 5, 7, 9, 3, 1, 3]
# print(li)
# li.reverse()
# print(li)
#
#
# # print("*" * 50)
# # print(keyword.kwlist)
#
#
# # 循环遍历
# i = 0
# li = [6, 5, 7, 9, 3, 1, 3]
# l = len(li)
# for i in range(0, l):
#     number = li[i]
#     print(number, '  ', end='')
#
# print('')
# # 列表嵌套
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


# i = 0
# j = 0
# while i < 5:
#     print('hello')
#     while j < 5:
#         print('hello')
#         continue
#         j += 1
#     i += 1
#     break

import random
school = [[], [], []]  # 定义学校和办公室
teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 定义教师信息

count_teacher = len(teacher)  # 获取teacher列表中的元素个数
count_school = len(school)   # 获取school列表中的元素个数

# 遍历teacher列表中的元素,追加到school[]中
for i in range(0, count_teacher):
    # 获取随机数
    result1 = random.randint(0, count_school)
    school[result1].append(teacher[i])
print(school)
