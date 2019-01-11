# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 字符串.py
# @Author: 杨崇
# @Date  : 2019/1/11
# @Desc  : null
# string = 'Python'
# # print(string[1])
# #
# # for i in string:
# #     print(i)
# #
#
#
# # 字符判断
# # string.isalpha()
# # 如果 string 至少有一个字符并且所有字符都是字母则返回 True
# str = 'python1'
# print(str.isalpha())
#
# # string.isdecimal() 	如果 string 只包含数字则返回 True
# str = '12345t'
# print(str.isdecimal())
#
# # string.islower()
# # 如果 string 中包含至少一个区分大小写的字符，
# # 并且所有这些(区分大小写的)字符都是小写，则返回 True
# str = 'ABC'
# print(str.islower())
#
# # string.isupper()
# # 如果 string 中包含至少一个区分大小写的字符，
# # 并且所有这些(区分大小写的)字符都是大写，则返回 True
# str = 'ABC'
# print(str.isupper())
#
# # string.startswith(str)
# # 检查字符串是否是以 str 开头，是则返回 True
# q = 'python'
# print(q.startswith(str))


# string.endswith(str)
# 检查字符串是否是以 str 结束，是则返回 True
# w = 'pytwon'
# print(w.endswith(w))


# string.find(str, start=0, end=len(string))
# 检测 str 是否包含在 string 中，
# 如果 start 和 end 指定范围，则检查是否包含在指定范围内，
# 如果是返回开始的索引值，否则返回 -1
# my_str = 'Python'
# print(my_str.find('t'))
# print(my_str.find('th1', 0, len(my_str)))


# 拆分和连接
# string.partition(str)
# 返回元组，把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
str = 'python@123.com'
print(str.partition('@'))
# print(str)


# string.rpartition(str)
# 类似于 partition() 方法，不过是从右边开始查找
str = '1234526'
print(str.rpartition('2'))


# string1 + string2 	拼接两个字符串
str1 = '123'
str2 = '456'
str = str1 + str2
print(str)

# string.split(str="", num)
# 返回列表，以 str 为分隔符拆分 string，如果 num 有指定值，
# 则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格
str = '123456'
print(str.split('3'))


# string.join(seq)
# 返回字符串，以 string 作为分隔符，
# 将 seq 中所有的元素（的字符串表示）合并为一个新的字符串


# 大小写转换
# string.lower() 	返回新字符串，转换 string 中所有大写字符为小写
# string.upper() 	返回新字符串，转换 string 中的小写字母为大写
str = 'aBcd'
print(str.lower())
print(str.upper())

# ItHeiMa  --  iThEImA
str = 'itheima'
str1 = 'iThEImA'
str2 = ''
for s in str1:
    if s.isupper():
        str2 += s.lower()
    else:
        str2 += s.upper()
print(str2)


# 文本对齐
str1 = 'python'
print(str1.ljust(20, '*'))

print(str1.center(20))

print(str1.rjust(20))

# 去除空白符
# string.lstrip() 	返回新字符串，截掉 string 左边（开始）的空白字符
# string.rstrip() 	返回新字符串，截掉 string 右边（末尾）的空白字符
# string.strip() 	返回新字符串，截掉 string 左右两边的空白字符
str = '   yc    '
print(str.lstrip())
str = '   yc    '
print(str.rstrip())
str = '   yc    '
print(str.strip())

# 切片
str = 'Python'
# 打印第一到第三的字符
print(str[0: 3])
print(str[3: 5])
print(str[3:])
print(str[:3])
print(str[1::2])



