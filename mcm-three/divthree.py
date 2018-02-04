import numpy as np
import pandas as pd
from countries import data

G = np.array(data)
#print(G)

# 选取3个点作为聚类中心
a, b, c = np.random.randint(0, 10, 3)
print(a,b,c)
print(G[a][0])
print(G[b][0])
print(G[c][0])
print('***************************************')
#print(G[a][1], G[b][1], G[c][1])
arr_c = list()
arr_c.append(G[a][1])
arr_c.append(G[b][1])
arr_c.append(G[c][1])

arr_c = list(map(float, arr_c))

last_G1 = np.array([[1]])
last_G2 = np.array([[1]])
last_G3 = np.array([[1]])
curr_G1 = np.array([[2]])
curr_G2 = np.array([[2]])
curr_G3 = np.array([[2]])
last_ar0 = 1
last_ar1 = 1
last_ar2 = 1
curr_ar0 = 0
curr_ar1 = 0
curr_ar2 = 0

while True:
    # 3组聚类
    G1 = []
    G2 = []
    G3 = []
    #print('**********')
    #print(last_G1)
    #print(curr_G1)
    #print(last_G2)
    #print(curr_G2)
    #print(last_G3)
    #print(curr_G3)
    #print('----------')
    #print((last_G1 == curr_G1).all())
    if last_G1.shape == curr_G1.shape and last_G2.shape == curr_G2.shape and \
        last_G3.shape == curr_G3.shape and (last_G1 == curr_G1).all()==True and \
            (last_G2 == curr_G2).all()==True and (last_G3 == curr_G3).all()==True:
        print('bingo')
        print(curr_G1)
        print(curr_G2)
        print(curr_G3)
        break
    if last_ar0 == curr_ar0 and last_ar1 == curr_ar1 and last_ar2 == curr_ar2:
        print('haha')
        print(curr_G1)
        print(curr_G2)
        print(curr_G3)
        break
    last_G1 = np.copy(curr_G1)
    last_G2 = np.copy(curr_G2)
    last_G3 = np.copy(curr_G3)
    # 计算数据集G中每个对象到聚类中心的距离
    for index in range(len(G)):
        x = np.abs(float(G[index][1])-arr_c[0])
        y = np.abs(float(G[index][1])-arr_c[1])
        z = np.abs(float(G[index][1])-arr_c[2])
        min_v = min(x, y, z)
        if min_v == x:
            G1.append(G[index])
        elif min_v == y:
            G2.append(G[index])
        elif min_v == z:
            G3.append(G[index])

    G1 = np.array(G1)
    G2 = np.array(G2)
    G3 = np.array(G3)
    G1x = list()
    G2x = list()
    G3x = list()

    #print(G1.shape)
    #print(G1)
    for index in range(G1.shape[0]):
        G1x.append(float(G1[index][1]))
    for index in range(G2.shape[0]):
        G2x.append(float(G2[index][1]))
    for index in range(G3.shape[0]):
        G3x.append(float(G3[index][1]))

    #print(G1x)

    # 计算每个对象的均值
    arr_c[0] = np.mean(G1x)
    arr_c[1] = np.mean(G2x)
    arr_c[2] = np.mean(G3x)
    #print(arr_c[0])
    #print(arr_c[1])
    #print(arr_c[2])
    curr_G1 = np.copy(G1)
    curr_G2 = np.copy(G2)
    curr_G3 = np.copy(G3)
    curr_ar0 = arr_c[0]
    curr_ar1 = arr_c[1]
    curr_ar2 = arr_c[2]

    #print('**********')
    #print(last_G1)
    #print(curr_G1)
    #print(last_G2)
    #print(curr_G2)
    #print(last_G3)
    #print(curr_G3)
    #print('----------')


print('over')

