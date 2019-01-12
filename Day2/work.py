# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : work.py
# @Author: 杨崇
# @Date  : 2019/1/12
# @Desc  : null

# 1.完成下列操作
list1 = ['xiaoming', 'xiaohua', 'xiaohong']
# (1)循环遍历出列表的所有元素
count = len(list1)
for i in range(0, count):
    print(list1[i])

# (2)把列表list2[“jack”,”marry”,”tom”]中的每个元素逐一添加到list列表中
list2 = ['jack', 'marry', 'tom']
list = []
count = len(list2)
for i in range(0, count):
    list.append(list2[i])
print(list)
# (3)查看list1列表是否有“xiaohua”这个元素
name = 'xiaohua'
if name in list1:
    print('存在')
else:
    print('不存在')

# (4)查看list1列表的长度
print(len(list1))


# 2.将下列两个列表合并，将合并后的列表升序并输出.
print('*' * 50)
list3 = [1, 3, 4, 5, 7]
list4 = [0, 66, 8, 9]
list3.extend(list4)
list3.sort()
print(list3)



# 3.使用字典来存储一个人的信息(姓名、年龄[数字]、学号)，
# 这些信息来自键盘的输入，储存完输出至终端.
name = str(input('姓名:'))
age = int(input('年龄:'))
number = str(input('学号:'))

user = {
    '姓名': name,
    '年龄': age,
    '学号': number
}
print(user)


# 4.有下列字典dict1,查找值为“itcast”对应的key并输出到终端.(结果应该是输出school)
dict1 = {'school': 'itcast', 'date': 2017, 'address': 'beijing'}
for my_dic in dict1:    # 去除字典中的每个元素的Key值('school', 'date', 'address')
    if dict1[my_dic] == 'itcast':   # dict1[my_dic] 字典.[key]  根据key获取对应的值, 然后跟 'itcast'做对比
        print(my_dic)    # 如果相等,说明dict1[my_dic] 中的my_dic 此时等于school


# 5.现有字符串： str1 = '1234567890'，根据题目要求完成以下题目：
str1 = '1234567890'
# （1）截取字符串的第一位到第三位的字符
print(str1[0:3])
# （2）截取字符串最后三位的字符
print(str1[-3:])
# （3）截取字符串的全部字符
print(str1[::1])


# 6.将下列字符串中所有的数字相加，相加完毕的结果输出至终端.
str2 ='10@20@30@4@6'
li = str2.split('@')
count = 0  # 和
for i in li:
    count += int(i)
print(count)


# 7.输出字符串str1中所有的偶数.
str3 = '1234567890'
for str in str3:
    if int(str) % 2 == 0:
        print(str)



