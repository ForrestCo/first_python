# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : oop.py
# @Author: 杨崇
# @Date  : 2019/1/3
# @Desc  : 面向对象


class myclass:
    i = 123456
    def d(self):
        return 'hello world!'

# 创建实例
x = myclass
print(x.i)
print(x.d(myclass))
