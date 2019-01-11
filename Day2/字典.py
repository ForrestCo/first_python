# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 字典.py
# @Author: 杨崇
# @Date  : 2019/1/10
# @Desc  : null

# user = {
#     'user_name': 'admin',
#     'user_pwd': '123456',
#     'number': '110'
# }
# user['age'] = '18'
# del user['age']
# user.pop('number')
# user.clear()
# print(user)
# print(len(user))
# user = {
#     'user_name': 'admin',
#     'user_pwd': '123456',
#     'number': '110'
# }
# user1 = {
#     'sex': '男',
#     'user_name': 'rose'
# }
# # 字典.setdefault(键，数据)  键值对不存在，添加键值对；存在则不做处理
# user.setdefault('age', '18')
# print(user)
#
# #  	字典.update(字典2)
# user.update(user1)
# print(user)

# li = [
#         {
#             'user_name': 'admin',
#             'user_pwd': '123456',
#             'number': '110'
#         },
#         {
#             'user_name': 'jack',
#             'user_pwd': '123',
#             'number': '123456'
#         }
# ]
# count = len(li)
# for i in range(0, count):
#     print(li[i])

# user = {
#     'user_name': 'admin',
#     'user_pwd': '123456',
#     'number': '110'
# }
# # 字典.get(键)
# # 根据键取值，键值对不存在不会报错
# print(user.get('user_name'))
#
# # 字典.keys() 	可进行遍历，获取所有键
# print(list(user.keys()))
#
# # 字典.values() 	可进行遍历，获取所有值
# print(list(user.values()))
#
# # 字典.items() 	可进行遍历，获取所有(键，值)
# print(user.items())

user = {
    'user_name': 'admin',
    'user_pwd': '123456',
    'number': '110'
}
#
# for key in user:
#     print(user[key])
#
#
# for i, j in user.items():
#     print(i, j)
#
# li = [
#         {
#             'user_name': 'admin',
#             'user_pwd': '123456',
#             'number': '110'
#         },
#         {
#             'user_name': 'jack',
#             'user_pwd': '123',
#             'number': '123456'
#         }
# ]
#
# count = len(li)
# for i in range(0, count):
#     user = li[i]
#     for a, b in user.items():
#         print(a, ':', b, ' ', end='')
#     print('')


card_list = [{"name": "张三",
              "qq": "12345",
              "phone": "110"},
             {"name": "李四",
              "qq": "54321",
              "phone": "10086"}
             ]
li = []
count = len(card_list)
for i in range(0, count):
    user = card_list[i]
    for key in user:
        if key == 'name':
            li.append(user['name'])
print(li)

for i in range(0, count):
    user = card_list[i]
    user['city'] = '北京'
print(card_list)

for i in range(0, count):
    user = card_list[i]
    for key in user:
        if user.get('name') == '张三':
            user['qq'] = '110110110'

print(card_list)
