import numpy as np 
import random
import matplotlib.pyplot as plt 
from sklearn.metrics.cluster import normalized_mutual_info_score


def ini_point(X):
    
all_data = np.loadtxt('data_2.csv')
correct_data = np.array(all_data)
Preconcern = np.array([[0,0,0]*5])
concern = np.array([all_data[np.random.randint(200)], all_data[np.random.randint(200,400)], all_data[np.random.randint(400,600)], all_data[np.random.randint(600,800)], all_data[np.random.randint(800,1000)]])

while True:
    Preconcern = concern
    for index, point in enumerate(all_data):
        distance = [np.linalg.norm(c - point) for c in Preconcern]
        minConcern = distance.index(min(distance)) + 1
        # print(minConcern)
        all_data[index,2] = minConcern
    concern = [np.mean([x for x in all_data if x[2] == 1], axis=0), 
                np.mean([x for x in all_data if x[2] == 2], axis=0), 
                np.mean([x for x in all_data if x[2] == 3], axis=0), 
                np.mean([x for x in all_data if x[2] == 4], axis=0), 
                np.mean([x for x in all_data if x[2] == 5], axis=0) ]
    judge = np.array([x for x in np.array(concern)[:,0:2] ==  np.array(Preconcern)[:,0:2]]).reshape(-1)
    if False in judge:
        Preconcern = concern
    else:
        break

## judgement indicator
result = correct_data[:,2] - all_data[:,2]
print("accuracy is %g"%(result[result == 0].size / result.size))

## NMI
print("NMI is %g"%normalized_mutual_info_score(correct_data[:,2],all_data[:,2]))
G1 = all_data[all_data[:,2] == 1].shape[0]
G2 = all_data[all_data[:,2] == 2].shape[0]
G3 = all_data[all_data[:,2] == 3].shape[0]
G4 = all_data[all_data[:,2] == 4].shape[0]
G5 = all_data[all_data[:,2] == 5].shape[0]
P_c = [200, 200, 200, 200, 200]
P_g = [G1, G2, G3, G4, G5]
Oij = np.array([[]],dtype=np.int32)
# H_d = -(np.sum(P_c*np.log(P_c/1000)))
# H_g = -(np.sum(P_g*np.log(P_g/1000)))

# draw picture
# fig = plt.figure()
# ax1 = fig.add_axes(211)
# ax2 = fig.add_axes(212)
# ax1.scatter(all_data[:,0], all_data[:,1], c = all_data[:, 2])
# plt.show()
