# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 元组.py
# @Author: 杨崇
# @Date  : 2019/1/10
# @Desc  : 元组

# 定义一个元组
# tu = ('jack', 12, ['张三', '李四'])
# print(tu)
# print(type(tu))
# print(tu[0: 2])
# print(tu[1:])
# print(len(tu))
# print(tu.index('jack'))
#
# if 'jack' in tu:
#     print('存在')
# count = len(tu)
#
# for i in range(0, count):
#     print(tu[i], end='')
# print('')
#
# a = 10
# b = 20
# a, b = b, a
# print(a, '  ', b)

# 组包, 拆包
# x = 1, 2
# print(type(x))
# print(x)
#
# tu = (1, 2, 3)
# a, b, c = tu
# print(a, b, c)
# tuple
#
# i = 2
# j = 3
#
# # 先从等号右边执行,首先 j 和 i 先进行组包(j, i),
# # 然后在进行解包赋值给 i, j
# i, j = j, i
# print(i, ' ', j)


# name = 'jack'
# age = 18
# tu = (name, age)
# print('我叫: %s, 今年:%d 岁' % tu)
#
#
# # 类型转换
# new_list = list(tu)
# print(type(new_list))

# 1.定义一个空列表 name_list,添加 xiaohong xiaoming xiaowang三个人名到列表当中
name_list = []
name_list.append('xiaohong')
name_list.append('xiaoming')
name_list.append('xiaowang')
print(name_list)

# 2.定义一个列表  names = ["zhansan","lisi","wangwu"],通过把names中的名字追加到第一个name_list列表当中
names = ["zhansan","lisi","wangwu"]
count = len(names)
for i in range(0, count):
    name_list.append(names[i])
print(name_list)
# 3.通过三种方法 分别删除 xiaohong,zhangsan,wagnwu
name_list.remove('xiaohong')
name_list.pop(2)
del name_list[3]
print(name_list)

# 4.逆序现在的name_list列表
name_list = ['xiaohong', 'xiaoming', 'xiaowang', 'zhansan', 'lisi', 'wangwu']
name_list.reverse()
print(name_list)
# 5.判断maliu 是否存在于name_list当中进行提示
if 'maliu' in name_list:
    print('存在')
else:
    print('不存在')




