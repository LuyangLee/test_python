import numpy as np 
import copy
import time
def statistics():
    b= np.arange(1, 13).reshape((3, 4))
    print(b)
    min_all = b.min()
    min_row = np.min(b, axis= 1)
    print(min_all)
    print(min_row)
    print(np.cumsum(b))
    print(b.T)
def create():
    za = np.zeros((2,4))
    print(za)
    ea = np.empty((2,4))
    ea_view = ea[:2]
    print(ea_view)
    print(ea)
    for row in ea:
        print(row)
    
def merge():
    a = np.array([[1,1,1],[1,1,1]])
    b = np.array([[2,2,2],[2,2,2]])
    print(a[:,:].shape)
    print(a[np.newaxis, :].shape)
    print(np.hstack((a, b)))
    t1 = time.time()
    a = a.ravel()
    t2 = time.time()
    print(a, '%f'%(t2 - t1))

def changeDim():
    a = ['hell',[1, 2, 3]]
    print(a)
    c = copy.copy(a)
    d = copy.deepcopy(a)
    a[1].append(4)
    a.append(5)
    print(c)
    print(d)

def myslice():
    a = np.arange(1,37).reshape((4, 9))
    a_view = a[:3, :1]
    print(a_view)
    # print(a[:3, 1:])
    print(a)

myslice()
