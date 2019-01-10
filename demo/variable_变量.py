# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : variable_变量.py
# @Author: 杨崇
# @Date  : 2018/11/9
# @Desc  : Python变量

# 多个变量赋值

# a = b = c = 1
# print (a, b, c)

a, b, c = 1, 2, "jack"
print(a, b, c)

'''
Python五个标准数据类型：
        Numbers(数字)、
        String（字符串）、
        List（列表）、
        Tuple(元祖)、
        Dictionary(字典)
'''

# Python数字
'''
 Python数字
 数字数据类型用于存储数值，是不可改变的数据类型，
 这意味着改变数字数据类型会分配一个新的对象；
 Python四种数字数据类型：
    int（整形）
    long (长整形)
    float (浮点型)
    complex (复数)

'''
var1 = 1
var2 = 2
print(var1, var2)
# 通过del语句删除一些对象的引用
del var1, var2
# print(var1, var2)

# Python字符串
'''

    从左到右索引默认0开始的，最大范围是字符串长度少1
    从右到左索引默认-1开始的，最大范围是字符串开头
    N  A  M  E
    0  1  2  3
   -4 -3 -2  -1

如果你要实现从字符串中获取一段子字符串的话，
可以使用 [头下标:尾下标] 来截取相应的字符串，
其中下标是从 0 开始算起，可以是正数或负数，
下标可以为空表示取到头或尾。
[头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。

    '''

s = "abcdefg"
print(s[0])  # 输出字符串中的第一个字符
print(s[0:3])  # 输出字符串中第一个到第五个之间的字符串
print(s[2:])  # 输出从第三个字符串开始的字符串
print(s * 2)  # 输出字符串2次
print(s + "yc")  # 输出拼接字符串




str1 = 'abcdefg'
# 输出第一个字符
print(str1[0])

# Python列表
'''
    List是Python中的列表类型，支持字符、数字、字符串
    还可以包含列表（嵌套）；
    列表使用[]标识
    列表中值的切割也可以用到变量 [头下标:尾下标] ，
    就可以截取相应的列表，从左到右索引默认 0 开始，
    从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

    t = ['a', 'b', 'c', 'd', 'e']
          0    1    2    3    4
   索引：
         -5   -4   -3   -2   -1 

    加号 + 是列表连接运算符，星号 * 是重复操作

'''
li = ['yc', 123, 3.14, 'jack', 30.9]
tiny = [345, 'jack']

print(li)  # 输出完整列表
print(li[0])  # 输出列表的第一个元素
print(li[0:3])  # 输出列表中第一个到第二个元素
print(li[2:])  # 输出第三个开始至列表末尾的所有元素
print(tiny * 2)  # 输出列表两次
print(li + tiny)  # 打印组合的列表

print(tiny)

# Python元祖
'''
    元祖类似于列表，元祖用 “（）”标识，内部元素用逗号隔开，
    相当于只读列表。

'''

my_tuple = ('yc', 123, 3.14, 'hu', 555)
ti_my_tuple = (123, 'fe')
print(my_tuple)  # 输出完整元组
print(my_tuple[0])  # 输出元组的第一个元素
print(my_tuple[1:3])  # 输出第二个至第三个的元素
print(my_tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(my_tuple * 2)  # 输出元组两次
print(my_tuple + ti_my_tuple)  # 打印组合的元组

# Python字典
'''
   字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
   列表是有序的对象集合，字典是无序的对象集合。 
   两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
   字典用"{ }"标识。字典由索引(key)和它对应的值value组成。 
'''

my_tiny = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(my_tiny['name'])  # 输出键为'name' 的值
print(my_tiny['name'])  # 输出键为 code 的值
print(my_tiny)  # 输出完整的字典
print(my_tiny.keys())  # 输出所有键
print(my_tiny.values())  # 输出所有值

# Python数据类型转换
'''
   有时候，我们需要对数据内置的类型进行转换，
   数据类型的转换，你只需要将数据类型作为函数名即可。
   以下几个内置的函数可以执行数据类型之间的转换。
   这些函数返回一个新的对象，表示转换的值。 
   
'''

