# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 面向对象.py
# @Author: 杨崇
# @Date  : 2018/11/10
# @Desc  : 面向对象

# 面型对象

'''
    语法：class className:
'''


class MyClass:
    i = 100
    def f(self):
        return 'hello word!'


# 创建实例
m = MyClass
print(m.i)

# 创建类
from click._compat import raw_input


class User:
    user_number = 0

    def __init__(self, username, password):  # 构造方法，在创建类的实例化对象时调用该方法
        self.username = username
        self.password = password

    def user_info(self):
        print("用户名：", self.username, )
        print("密  码：", self.password)

    def main(self):
        self.username = raw_input("请输入用户名：")
        self.password = raw_input("请输入密码：")
        print("您输入的用户名为：", self.username)
        print("您输入的密码为：", self.password)

user = User("admin", "123")
user.user_info()
user.main()


"""
class Person:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex

        self.age = age
        print(name, sex, age)

    @staticmethod
    def run():
        print("每天早上跑步")

    @staticmethod
    def eat():
        print("跑完步吃饭")


p = Person("小明", "男", "18")
p.run()
p.eat()
print("-----------------------")
p1 = Person("小美", "女", "18")
p.run()
p.eat()

"""


# python对象销毁(垃圾回收)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")


pt1 = Point
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # 打印对象的id
del pt1
del pt2
del pt3


# 类的继承
# class 派生类（基类名）
# ...
# 定义父类
class Parent:
    parentAttr = 100

    def __init__(self):
        print("父类构造函数被调用")

    @staticmethod
    def parentMethod():
        print("父类方法被调用")

    @staticmethod
    def setAttr(attr):
        Parent.parentAttr = attr

    @staticmethod
    def getAttr():
        print("父类属性 :", Parent.parentAttr)
