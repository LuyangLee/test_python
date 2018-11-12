import random
from sklearn import datasets
import math
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#定义距离
def vecDistance(vector1, vector2):
    return math.sqrt(math.pow((vector1 - vector2), 2))

#选择质心
def initCenter(dataSet, k_value):
    sampleNum, dim = dataSet.shape
    center = np.zeros((k_value, dim))
    for i in range(k_value):
        index = int(random.uniform(0, sampleNum))
        center[i,:] = dataSet[index, :]
    return center

def kmeans_train(dataSet, k_value):
    sampleNum = dataSet.shape[0]
    groupUse = np.mat(np.zeros((sampleNum, 2))) #第一列表示数据类别，第二列表示到样本中心差
    #先初始化质心
    center = initCenter(dataSet, k_value)
    distance = np.zeros((sampleNum, k_value))
    draw(dataSet, center)
    new_center = np.zeros_like(center)
    num_iter = 10000
    # 开始计算当前样本点到质点的距离
    for _ in range(num_iter):
        for i in range(sampleNum):
            distance[i] = np.sqrt((center - dataSet[i]) ** 2).sum(axis=1).reshape(1, k_value)
        classes = np.argmin(distance, 1)
        for k in range(k_value):
            sample = dataSet[classes == k]
            new_center[k] = sample.mean(axis=0)
        delta = np.sqrt((center - new_center)**2).sum()
        if delta < 1e-6:
            break
        center = new_center
    return center, classes
        # for i in range(sampleNum):
        #     minDis = 10000.0
        #     minIndex = 0
        #     for j in range(k_value):
        #         nowDis = vecDistance(dataSet[i:], center[j:])
        #         if nowDis < minDis:
        #             minDis = nowDis
        #             minIndex = j

def draw(dataSets, center,):
    ax = plt.figure(111)
    plt.scatter(dataSets[:,0], dataSets[:, 1])
    plt.scatter(center[:, 0], center[:, 1], color='red')
    plt.show()

def judgeCost(dataSets, center, k_value):
    sampleNum , dim = dataSets.shape
    distance = np.zeros((sampleNum, k_value))
    for i in range(sampleNum):
        distance[i] = np.sqrt((center - dataSets[i]) ** 2).sum(axis=1).reshape(1, k_value)
    cluster = np.argmin(distance, axis=1)
    result = 0
    for k in range(k_value):
        sample = distance[cluster == k]
        result += ((sample - center[k])**2).sum()
    return result

data = pd.read_csv('test.txt', header=None)
print(data)
center,classes = kmeans_train(np.array(data), 4)
print(center)
print(classes)
draw(np.array(data), center)

