# python基础学习

## 1.函数

### 1.1 基本形式

```python
def function_name():
    ...
    return
```

### 1.2参数形式

#### 1.2.1基本参数

```python
def funtion_name(a, b):
    ...
    return
```

调用的时候小技巧就是fun（a = ..., b = ...），这样可以不用管参数的位置

#### 1.2.2默认参数

```python
def funtion_name(a, b=4, c='xiaoming'):
    ...
    return
```

注意的是，默认参数不应该在正常参数之前，

#### 1.2.3 自调用

```python
if __name__== '__main__':
    #调用函数
```

如果执行脚本的时候，里面可以加上单元测试的代码，可以测试这个文件中的函数。

若作为模块对外调用的话，那么就不会执行，比较方便。

#### 1.2.4可变参数

```python
def funtion_name(a, b=5, *grades):
    for grade in grades:
        ...
    return
```

可变参数不应该出现在普通参数和默认参数前面，否则会被覆盖，**参数可以用，隔开依次传入**形成可迭代序列。

#### 1.2.5 关键字参数

```python
def funtion_name(name,**kw):
    for key,value in kw:
        ...
    return
```

关键字参数对应着字典，**使用key = values,注意形如country = 'England'这样前面key不要加引号表示参数**

#### 1.2.6 总结

> 总之，所有函数参数都可以用funtion_name(*args, **kw)来表示

### 2 变量

```python
a = None
def fun():
    global a
    b = 30
    a = 20
    return
```

这里**a**是全局变量，b是局部变量

### 3文件读取

```python
#添加语句
def addFile():
    text = 'IloveChina\nI feel so nice\nhow are you?'
    myfile = open('test5.txt','a')
    myfile.write(text)
    myfile.close()
#读取文件,三种方式
def readFile():
    myfile = open('test5.txt','r')
    contextList = myfile.readlines()
    #contextLine = myfile.readline()
    #context = myfile.read()S
    print(contextList)
```

### 4 类

```python
class Calculator（Object）:       #首字母要大写，冒号不能缺
    name='Good Calculator'  #该行为class的属性
    price=18
    def add(self,x,y):
        result = x + y
        print result
        
cal = Calculator()
cal.price
```

注意事项如下：（1）、类的**首字母大写**，类内分为函数和属性，**属性要赋值**

​			（2）、定义方法的时候一定要注意**第一个参数要加self**

​			（3）、调用的时候不用new，直接是类名＋（），属性和方法调用同其他语言

#### 4.1 init方法

```python
class Calculator:
    name = 'mycaculator'
    price = 19
    def __init__(self,name, price,high):
        self.name = name
        self.price = price
        self.high = high
cal = Calculator()
#检查是否有某个属性
hasattr(cal,'price')
#添加属性（或者更改如果有的话）
setattr(cal,'height',13)
#删除属性
delattr(cal,'height')
cal.h
del cal
```

注意事项如下：（1）、类的init方法中**新增的属性是类内的属性**，不管外面有没有声明。

​			（2）、删除使用del。

​			（3）、类的动态属性在类内类外都可以直接添加，但是在外面通过实例添加 的时候类本身不添加上。

### 5基本类型

#### 5.1list和tuple的基本方法

```python
list = [1,3,'dd',3.2]
tuple = (1,3,'dd',3.2)
#待添加值定义为value
#添加
list.append(value)#末尾添加
list.insert(index,value)#指定位置添加
#删除
list.pop()#删除末尾元素
list.pop(i)#删除指定位置元素
list.remove(i)#删除制定位置的元素
#修改
list[index]  = value
#片选(结果还是list)
list[:]
#某个值的索引号
list.index(value)#返回的是某个值的索引
#某个值出现的次数
list.count(value)
#排序
list.sort()
list.sort(reverse = True)
#迭代
for index,value in enumrate(list)
```

#### 5.2 字典

字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#查找
d['Bob']
'Bob' in d #查询某个关键字是否在字典中
#迭代
for key,value in d.items()
```

值得注意的是key**一定是不可变变量**

#### 5.3 字符串

```python
t = 'wo ai ni'  #unicode编码形式
bt = b'wo ai ni' #byte流形式
t.encode('ascii'或者'utf-8')
bt.decode('ascii'或者'utf-8')
len(t) #t中字符个数
'wo {0} ni'.format('ai') #{0}表示占位符
t = t.replace('ai','AI')
```

注意replace函数返回一个字符串，因为字符串属于静态变量，所以必须让变量**重新指向字符串**。

#### 5.4 切片，列表生成式

```python
#切片
[ia:ib:numc]#从a的位置开始，到b位置之前，每次隔c个1（不是间隔而是隔）
#列表生成式
[x * x for x in range(1, 11) if x % 2 == 0] #快速生成一个list，可以对于循环得出的每个元素运算后形成列表list
#生成器
g = (x * x for x in range(10))
使用next(g)获取每个元素
#生成器函数
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a + b
        n = n+1
    return 'done'
使用对象来获取每个元素 f = fib(10)		 next(f)
```

### 5.4 set集合

```python
s = set([1,2,3])
another  = set([1,5])
theother = set([2,5])
s.difference(another)#找出s中不含another里面内容的集合
s.intersection(theother)#找出s中与theother里面内容相同的集合
```

注意事项：set集合声明**一定要加set**，里面传入的是list作为参数，最终结果为{1,2,3}

​		set**最终的结果是{1,2,3}**，相当于没有key只有value的字典

## 6 import的用法

```python
#import name,这个模块可以自带，也可以是安装好的库
import time
print(time.time())
#import name as _ '_'表示可以自己把name定义为其他的名字
import numpy as np
print(np.zeros())
#from time import time, localtime ，引用自己想要的功能一般是函数，属性什么的
from time import time, localtime
print(localtime())
print(time())
#from time import * 等价于输入模块的所有功能,区别在于不用加前缀了
from time import *
print(localtime())
```

## 7 错误处理

```python
#try...except...as...//首先检查文件打开问题，再检查在文件打开之后的问题，再关闭文件
try:
    file = open('eee.txt',r)
except Exception as e:
    print(e)
    exit(-1)
try:
    接着打开文件之后的检查错误
except Exception as e:
    print(e)    
finally:
    file.close()
#以上语句可以用with...as...代替
with open('eee.txt',r) as file:
    data = file.read()
    
#在自定义类中的推广如下：
class Sample:  
    def __enter__(self):  
        print "In __enter__()"  
        return "Foo"  
   
    def __exit__(self, type, value, trace):  
        print "In __exit__()"  
with Sample() as sample:  
    #你的要检查的语句块

```

​	with使用的精髓在于：可以将事前工作，事后处理工作独立出去成为entry和exit，就是针对要检查的语句块避免再写except和finally。

注意事项：（1）、注意finally是为了保证在try执行出问题时，一定会执行finally中语句。

​		（2）、注意文件打开的**两次try**

## 8特殊关键字

### 8.1zip

```python
#zip接收任意多个（0,1）也可以作为参数，把他们压缩成一个tuple
zip(序列1，序列2)
```

### 8.2 lambda

```python
#lambda定义了一个匿名函数，定义的方法同函数一样(少了括号和返回值)
fun = lambda x,y:x + y
```

### 8.3 map

```python
#map表示把参数列与函数进行绑定
def fun(x, y):
    x + y
map(fun,[x],[y])
```

## 9字符串匹配

写在[]里面用来匹配的：

> - \d : 任何数字
> - \D : 不是数字
> - \s : 任何 white space, 如 [\t\n\r\f\v]
> - \S : 不是 white space
> - \w : 任何大小写字母, 数字和 “*” [a-zA-Z0-9*]
> - \W : 不是 \w
> - \b : 空白字符 (**只**在某个字的开头或结尾)
> - \B : 空白字符 (**不**在某个字的开头或结尾)
> - \\ : 匹配 \
> - . : 匹配任何字符 (除了 \n)
> - ^ : 匹配开头
> - $ : 匹配结尾
> - ? : 前面的字符可有可无

写在后面用来匹配的：

> - `*` : 重复零次或多次
> - `+` : 重复一次或多次
> - `{n, m}` : 重复 n 至 m 次
> - `{n}` : 重复 n 次

```python
import re
pattern = r"匹配模式"
print(re.search(pattern, 匹配字符串), flags = re.M)#多行匹配
print(re.findall(pattern, 匹配字符串))#找到所有的字符匹配
print(re.sub(pattern, "更改字符串", 匹配字符串))# 讲匹配之后的替换掉
```

更详尽的参考[https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html]()



