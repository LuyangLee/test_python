import numpy as np 
import random
import matplotlib.pyplot as plt 
from sklearn import svm
from sklearn.model_selection import train_test_split
from scipy import stats
sigma = [[1, 0],[0, 1]]
mu1 = [1, -1]
mu2 = [5, -4]
mu3 = [1, 4]
mu4 = [6, 4.5]
mu5 = [7.5, 0.0]
thetaIndex = []
result = []
x1 = np.random.multivariate_normal(mean= mu1, cov = sigma, size=200)
x2 = np.random.multivariate_normal(mean= mu2, cov = sigma, size=200)
x3 = np.random.multivariate_normal(mean= mu3, cov = sigma, size=200)
x4 = np.random.multivariate_normal(mean= mu4, cov = sigma, size=200)
x5 = np.random.multivariate_normal(mean= mu5, cov = sigma, size=200)
xy1 = np.concatenate((x1,[[1]]*200), axis=1)
xy2 = np.concatenate((x2,[[2]]*200), axis=1)
xy3 = np.concatenate((x3,[[3]]*200), axis=1)
xy4 = np.concatenate((x4,[[4]]*200), axis=1)
xy5 = np.concatenate((x5,[[5]]*200), axis=1)
random.shuffle(xy1)
random.shuffle(xy2)
random.shuffle(xy3)
random.shuffle(xy4)
random.shuffle(xy5)
all_data =np.concatenate((x1,x2,x3,x4,x5))
traindata1 = np.concatenate((xy1[0:40],xy2[0:40],xy3[0:40],xy4[0:40],xy5[0:40]))
traindata2 = np.concatenate((xy1[40:80],xy2[40:80],xy3[40:80],xy4[40:80],xy5[40:80]))
traindata3 = np.concatenate((xy1[80:120],xy2[80:120],xy3[80:120],xy4[80:120],xy5[80:120]))
traindata4 = np.concatenate((xy1[120:160],xy2[120:160],xy3[120:160],xy4[120:160],xy5[120:160]))
testdata1 = np.concatenate((xy1[160:200],xy2[160:200],xy3[160:200],xy4[160:200],xy5[160:200]))

# plt.plot(x1[:,0], x1[:,1], 'x')
# plt.axis('equal')
# plt.show() 
# 设置类别的标签
# data_target = [1]*200 + [2]*200 + [3]*200 + [4]*200 +[5]*200

thetaList = [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10]

def train(traindata, theta):
    x_train, x_test, y_train, y_test = train_test_split(traindata[:,0:2], traindata[:,2], test_size = 0.4 )
    right_propor = 0.0
    suit_theta = theta[0]
    for c in theta:
        svc = svm.SVC(C= c, kernel='linear')
        svc.fit(x_train, y_train)
        y_pred = svc.predict(x_test)
        count = 0
        for y_index, y_t in enumerate(y_test):
            if y_pred[y_index] == y_t:
                count += 1
        if (count)/len(y_test) > right_propor:
            right_propor = (count)/len(y_test)
            suit_theta = c
    return (suit_theta,right_propor)

def findPro_C(looptimes):
    cSets = []
    for _ in range(0,looptimes):
        c1, rProp1 = train(traindata1, thetaList)
        c2, rProp2 = train(traindata2, thetaList)
        c3, rProp3 = train(traindata3, thetaList)
        c4, rProp4 = train(traindata4, thetaList)
        cSets = cSets + [c1,c2,c3,c4]
    return stats.mode(cSets)[0]

avg_param = findPro_C(5)
c, pro = train(testdata1, avg_param)
print('avg param:',  avg_param)
print('正确率： ',pro)
# for theta in range(1, 1000):
#     thetaIndex.append(theta*0.01)
#     result.append(traindata(theta*0.01))

# plt.plot(thetaIndex, result)
# plt.xlabel('正则化系数')
# plt.ylabel('正确率')
# plt.show()


