# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : 运算符.py
# @Author: 杨崇
# @Date  : 2018/11/9
# @Desc  : 运算符


# Python运算符

"""
    算术运算符
    比较运算符
    赋值运算符
    逻辑运算符
    位运算符
    成员运算符
    身份运算符
    运算符优先级
"""

# Python算术运算符
"""
    + 加
    - 减
    * 乘
    / 除
    % 返回除法的余数
    ** 幂
    // 返回商的整数部分（向下取整）
"""

x = 21
y = 10
z = 0

print("x+y=", x + y)
print("x-y=", x - y)
print("x*y=", x * y)
print("x/y=", x / y)
print("x%y=", x % y)
print("x**y=", x ** y)
print("x//y=", x // y)


# Python比较运算符
'''
    ==  --等于-比较对象是否相等
    !=  --不等于-比较对象是否不相等
    <>  --不等于-比较对象是否不相等
    >   --大于-比较X是否大于Y
    <   --小于-比较X是否小于Y
    >=  --比较X是否大于等于Y
    <=  --比较X是否小于等于Y
'''
x = 21
y = 10
c = 0

if x == y:
    print("x等于y")
else:
    print("x不等于y")

if x != y:
    print("x不等于y")
else:
    print("x等于y")

if x != y:
    print("x 不等于 y")
else:
    print("x 等于 y")

if x < y:
    print("x小于y")
else:
    print("x大于y")

if x > y:
    print("x大于y")
else:
    print("x小于y")


# Python赋值运算符
'''
    =   --简单的赋值运算符  c = a + b 将 a + b 的运算结果赋值为 c
    +=  --加法赋值运算符  c += a 等效于 c = c + a
    -=  --减法赋值运算符   c -= a 等效于 c = c - a
    *=  --乘法赋值运算符   c *= a 等效于 c = c * a
    /=  --除法赋值运算符   c /= a 等效于 c = c / a
    %=  --取模赋值运算符   c %= a 等效于 c = c % a
    **= --幂赋值运算符    c **= a 等效于 c = c ** a
    //= --取整除赋值运算符  c //= a 等效于 c = c // a
'''


# Python逻辑运算符
'''
    and
    or
    not --not x 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
'''


# Python成员运算符
'''
    in --如果在指定的序列中找到值返回 True，否则返回 False。
    not in --如果在指定的序列中没有找到值返回 True，否则返回 False
'''
a = 10
b = 20
demo = [1, 2, 3, 4, 5]

if a in demo:
    print("变量 a 在给定的列表中 demo 中")
else:
    print("变量 a 不在在给定的列表中 demo 中")

if a not in demo:
    print("变量 a 不在给定的列表中 demo 中")
else:
    print("变量 a 在在给定的列表中 demo 中")


# Python身份运算符
'''
    is	--is 是判断两个标识符是不是引用自一个对象	
             x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False；
             
    is not	--is not 是判断两个标识符是不是引用自不同对象	x is not y ， 
                     类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
             
    is 与 == 区别：
    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。        
        
'''
a = [1, 2, 3]
b = a
b is a   # true
b == a  # true


b = a[:]
b is a  # false
b == a  # true
