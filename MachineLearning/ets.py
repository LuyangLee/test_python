import numpy as np 
num_classes = 10
#需要转换的整数
arr = np.array([1,2,1,2,2])-1
#将整数转为一个10位的one hot编码
print(np.eye(5)[arr])