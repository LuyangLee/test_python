import math as mt 

def Plist():
    # 元组
    la = ['xiaoming', '12']
    lb = ['run', 263, 3.4j]
    # 打印两遍（但是在一个列表中）
    print(la * 2)
    #组合打印
    print(lb + la)
    #选取打印
    print(lb[:1])

def Ptuple():
    #列表同上
    ta = (1,'xiaoming', 5.4)

def Pdict():
    #字典
    da = {'name':'join', 'age':13, 'salary': 5200}
    #字典添加
    da['adress'] = 'BeiJing'
    #输出键值
    print(da.keys())
    print(da.values())
    print(da)

def transType():
    ia = 15
    fa = 1.5
    ca = 'a'
    print(ord(ca))
    print(hex(ia))
    print(type(hex(ia)))

def isUsage():
    # 这个时候b传给a传递的是引用
    a = b = [1,2,3]
    # 这个时候传递是拷贝
    b = a[:]
    #is 相当于判断是不是同一块内存，是不是同一个地址； == 相当于判断值是不是相等
    print(a is b)
    print(a == b)

def addFile():
    text = 'IloveChina\nI feel so nice\nhow are you?'
    myfile = open('test5.txt','w')
    myfile.write(text)
    myfile.close()

def readFile():
    myfile = open('test5.txt','r')
    contextList = myfile.readlines()
    print(contextList)

class Calculator:
    name = 'mycaculator'
    price = 19
    def __init__(self,name, price,high):
        self.name = name
        self.price = price
        self.high = high

cal = Calculator('xiaohong',19,18)
print(cal.high)

