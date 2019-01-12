# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 内置函数.py
# @Author: 杨崇
# @Date  : 2019/1/11
# @Desc  : null

# 内置函数

# 删除变量
i = '2'
print(i)
del(i)
del(i)

# max(item)
# 返回容器中元素最大值 	如果是字典，只针对 key 比较
li = [1, 2, 3, 26]
print(max(li))

user = {
    'age': 'tfyufyftd',
    'height': '180'
}
print(max(user))


# 切片
li = [1, 2, 3, 4, 5]
print(li[:3])


# else搭配循环使用:
#       没有通过 break 退出循环，循环结束后，会执行的代码
students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

for i in range(0, 10):
    print(i)
else:
    print('被执行')

# 使用场景
# input_name = str(input("请输入姓名:"))
# for user in students:
#     if input_name == user['name']:
#         print('找到了')
#         break
# else:
#     print('没找到')

dict = {'a':1,'b':2}
dict.get('c',3)
print(dict.get('c',3))