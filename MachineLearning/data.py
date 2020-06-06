import numpy as np 

def generateData():
    sigma = [[1, 0],[0, 1]]
    mu1 = [1, -1]
    mu2 = [5, -4]
    mu3 = [1, 4]
    mu4 = [6, 4.0]
    mu5 = [7.0, 0.0]
    x1 = np.random.multivariate_normal(mu1, sigma, size= 200)
    x2 = np.random.multivariate_normal(mu2, sigma, size= 200)
    x3 = np.random.multivariate_normal(mu3, sigma, size= 200)
    x4 = np.random.multivariate_normal(mu4, sigma, size= 200)
    x5 = np.random.multivariate_normal(mu5, sigma, size= 200)
    raw_data = np.concatenate((x1, x2, x3, x4, x5), axis = 0)
    label = np.concatenate(([[1]]*200, [[2]]*200, [[3]]*200, [[4]]*200, [[5]]*200), axis = 0)
    all_data = np.concatenate((raw_data, label), axis = 1)
    np.savetxt('data_2.csv', all_data)

if __name__ == "__main__":
    generateData()
