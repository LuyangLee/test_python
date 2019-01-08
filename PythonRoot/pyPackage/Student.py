import numpy as np
import math

sum(,)

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_score(self, score):
        if score > 100 or score < 0:
            raise ValueError("bad score")
        else:
            self.__score = score

#设置数组的类型
# datatype = np.dtype(np.int32)
# dt2 = np.dtype([('age',np.int8)])
# dt3 = np.dtype([('name','S20'),('age',np.int8)])

# b = np.array([[1,2] , [2,3]],dtype = dt2)
# c = np.array([('xiaoming',12),('xiaohong',13)],dtype = dt3)
# print(datatype)
# print(c)

#数组的创建
#             

#np.shape() 返回一个数组的维度元组（D1，D2,..,Dn）  np.reshape()调整数组的维度
#np.ndim()返回数组的维度    
#np.itemsize()返回每个元素字节大小
#np.formbuffer((buffer, dtype = float, count = -1, offset = 0) 将buffer构造成为一个一维的数组
#numpy.arange(start, stop, step, dtype) 构造一个一维的数组
#索引(索引是每个方框内的元素和下一个方框内的组合)
a = np.array([[1,2,3],[4,5,6]],dtype = 'i2')
print(a)
y = a[[1,1],[1,2]]
print(y)
