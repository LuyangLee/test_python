import pandas as pd 
import numpy as np 

# if None:
#     print("false")
# else:
#     print("true")

s = r"a\\nAB*7"
d = "sadfDS"
hSpace = " asdcf "
now = hSpace.strip()
print(now)
print("%s is %d"%('xiaoming', 10))
print("{} is {}, {}".format("xiaoming", 10, "dudu"))


l = ["1", '2', '3', '4']
y = ['10', '11', '12']
print(l)
l = l[::-1]
print(l)
l.reverse()
print(l)
# l.extend(y)
# print(l)
a = ",".join(l)
print(a)

for index, item in enumerate(l):
    print(index, item)

