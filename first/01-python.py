# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 01-python.py
# @Author: 杨崇
# @Date  : 2019/1/6
# @Desc  : null
import pymysql

# print("*****************Hello World!*************************")
# a = 100
# b = 10
# print('a的值为：', a)
# print(a + b)
# print(a - b)
# print(a % b)
# print(a / b)
# print(a * b)
# print(a ** b)

# 迭代器
from raven.utils import json

# list1 = [1, 2, 3, 4]
# 创建迭代器对象
# it = iter(list1)
# print(list1.__len__())
# 循环输出list1中的元素
# for i in list1:
#     print(next(it))

# 创建元组，元组中的元素不可修改
# tup1 = (1, 2, 3, 4, 5)
# 修改元组中的元素运行报错
# tup1[0] = 100
# 创建迭代器对象
# it1 = iter(tup1)
# 循环迭代输出
# for x in tup1:
#     print(next(it1))


'''
print("hello world")
'''
# print("hello world")

"""
print("hello world")
"""

""" 
# 定义变量
username = input("请输入用户名：")
password = input("请输入密码：")

# 小明信息
name = "小明"
age = 18
sex = "男"
height = 175.5
weight = 75.5
isdelete = False

if username == "admin" and password == "123456":
    print("用户登陆成功")
else:
    print("用户名或密码错误！")

if username == "admin":
    if password == "123456":
        print("登陆成功！")
        print(name, age, sex, height, weight, isdelete)
    else:
        print("密码错误")
else:
    print("用户名错误")
"""
"""
edibles = ["1", "2", "3", "4"]
for food in edibles:
    if food == "2":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")

"""

"""
# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()
"""

# 面向对象
"""

    1、类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    2、类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    3、数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
    4、方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    5、局部变量：定义在方法中的变量，只作用于当前实例的类。
    6、实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
    7、继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    8、实例化：创建一个类的实例，类的具体对象。
    9、方法：类中定义的函数。
    10、对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""

"""
# 定义一个类
class Demo:
    str1 = "jack"

    #  构造函数
    def __init__(self):
        print("构造函数被调用！")


# 对象实例化
d = Demo()
print(d.str1)
"""


# 创建所有员工的基类
class Emp:
    count = 100
    # username = None
    # password = None

    #     构造函数
    def __init__(self, username, password):
        self.username = username
        self.password = password
        Emp.count += 1

    def demo1(self):
        print("count的值为：%d" % self.count)

    def demo2(self):
        print("username:", self.username, "password:", self.password)


# 创建实例对象
# 每创建一次实例对象就会调用一次构造函数
e1 = Emp("admin", "123456")
e2 = Emp("admin", "123456")
print(Emp.count)

"""
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

"""