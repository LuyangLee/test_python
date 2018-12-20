import sys


# 需要检测的语句
try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except ValueError as ve:
    print("can't convert{0}".format(ve))
except OSError as ose:
    print("OS error {0}".format(ose))
    raise
else:
    print(i)
    f.close()
    

# 自定义异常类
class fooErro(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'value is %d'%self.value
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise fooErro(0)
    return 10/ n

foo(0)