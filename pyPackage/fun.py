#位置参数
def mymax(x, y):
    if not isinstance(x,(int , float)) and not isinstance(y, (int, float)):
        raise TypeError("bad operator")
    if x>y:
        return x
    else:
        return y

def myfun(x):
    pass

#默认参数
def add_end(m = None):
    if m is None:
        m = []
    m.append('End');
    return m

#可变参数（参数为list和tuple） 推荐参数名称用args
def myadd(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

#关键字参数(参数为dict) 推荐参数名用kw
def info(age,**kw):
    if 'gender' in kw:
        print("东方月初？")
    if 'power' in kw:
        print(kw['power'])

#关键字参数+可变参数
def person(name, *, city = 'Beijing', job):
    print(name, city, job)

#递归
def fact_iter(n, factor):
    if n == 1:
        return factor
    else:
        return fact_iter(n - 1, n*factor)

#汉诺塔式递归
def hanoi(num, A, B, C):
    if num == 1:
        print('move', A, '->', C)
    else:
        hanoi(num - 1, A, C, B)
        print('move', A, '->', C)
        hanoi(num - 1, B, A, C)

#去掉收尾的空格
def trim(pstr):
    flag = 0
    begin = 0
    numOfLast = 0
    for x in pstr:
        if x == ' ' and flag == 0:
            begin += 1
        elif x != ' ':
            flag = 1
            numOfLast = 0
        elif x == ' ' and flag == 1:
            numOfLast += 1
    return pstr[begin:len(pstr) - numOfLast]

#去掉首尾空格双向版
def trim2(pstr):
    while(pstr[0] == ' '):
        pstr = pstr[1:]
    while(pstr[len(pstr) - 1] == ' '):
        pstr = pstr[:len(pstr) - 1]
    return pstr
#迭代dict
def printall(d):
    for k,v in d.items():
        print(k,'-->',v)

#发现最大最小值(list中)
def finMinandMax(L):
    if L is None:
        return (None,None)
    else:
        max = L[0]
        min = L[0]
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return (min, max)

#杨辉三角
def triangels():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)]  + [1]  