#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn import datasets
from fun import mymax
from collections import Iterable
import fun
import math
import os,sys
iris = datasets.load_iris()
x = iris.keys

oct_i = 0o71 #八进制
hex_i = 0x71 #十六进制
ord_i = 71  #十进制

pstr = '123'
NTW = r'\\\daew\n'
ML = '''line1
line2
line3'''
#编码问题
tStr = "日照香炉"
tbyte = b'\xe4\xb8\xad\xff'
#list等集合
classmate = ['小明','小红','小兰']
#print('人数',len(classmate),'第一个人',classmate[0],'最后一个人',classmate[-1])
classmate.append('小白')
classmate.pop()
classmate.insert(3,'小白')
classmate[3] = '小灰'
#tuple
schoolmate = ('小明','小红','小兰')
student = ('小明',)
#格式化输出
#print('the growth rate is:%% %d'%25)
#print('{0}the growth rate is:{1:.1f}'.format('小明',18.75))

# weight = input("你的体重:")
# weight = int(weight)
# if weight < 80:
#     print(weight)
# elif weight < 90:
#     print(weight)
# else:
#     print('overweight')

#循环输出
# sum = 0
# for x in classmate:
#     print(x)
# for x in range(10):
#     sum = sum + x
# print(sum)

#字典
# d = {'小明':95, '小红':98}
# print(d['小明'])
# d['小兰'] = 99
# print(d['小兰'])

#set
# s = set([1, 2, 2, 3])
# print(s)

#调用可变参数
# mylist = (1,2,3,4,5)
# print(fun.myadd(*mylist))

# fun.info(16,gender = '男',power = 100)
# print(fun.myadd(1,2,3,4))

#切片
# number = [0,1,2,3,4,5]
# a = number[1:3] #表示1,2号元素
# b = number[-2:-1] #表示倒数第二号元素
# c = number[:4:2]
# print(a,b,c)

#print(isinstance(pstr,Iterable))
#fun.printall(d)

#列表生成式(相当于把迭代元素再处理, 好处就是在迭代的时候，生成的是中间项而不是在原有的变量上操作）
c = [ x + y for x in 'ABC' for y in 'XYZ']
d = [ x for x in os.listdir('.')]

#生成器
# g = (x *x for x in range(1,10))
# print(g)


# 循环:
# it = iter([1, 2, 3, 4, 5])
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break
print(sys.path)
