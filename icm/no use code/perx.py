"""
计算皮尔逊相关系数
"""
import numpy as np
import pandas as pd
import xlrd
import math
from ccpi import fragile

# 各国的脆弱性量化值
frag = np.array(fragile)
#print(frag)
# 20项指标读取
data = pd.read_excel('./resource/data2014.xlsx')
#print(frag)
print('*****************************')
#print(data)

# X 脆弱性值数列
# 计算脆弱性值的期望
EX = 0
for index in range(len(fragile)):
    EX = EX + float(fragile[index][1])

EX = EX / len(fragile)
#print(EX)

nrows, ncols = np.shape(data)

# 求每个指标的期望
#print(data.values[:nrows-3,:])
# 剔除Excel最后三行数据
G = data.values[:nrows-3,:]
EY = list()
for col in range(1, ncols):
    E = 0
    for row in range(nrows-3):
        E = E + float(G[row][col])
    E = E / (nrows - 3)
    EY.append(E)

#print(EY)

# D(X) X方差
DX = 0
for index in range(len(fragile)):
    DX = DX + (float(fragile[index][1])-EX)**2
DX = DX / len(fragile)
#print(DX)

# 计算E(XY)期望
EXY = list()
for col in range(1, ncols):
    E = 0
    for ix in range(len(fragile)):
        for iy in range(nrows-3):
            E = E + (float(fragile[ix][1]) * float(G[iy][col]) / (len(fragile)*(nrows-3)))
    EXY.append(E)

#print(EXY)
# 计算D(Y)
DY = list()
for col in range(1, ncols):
    D = 0
    for row in range(nrows-3):
        D = D + (float(G[row][col])-EY[index])**2
    D = D / (nrows-3)
    DY.append(D)

#print(DY)


# 计算相关系数
Pxy = list()
for index in range(ncols-1):
    Pxy.append((EXY[index] - EX*EY[index])/(math.sqrt(DX)*math.sqrt(DY[index])))

print(Pxy)

#print(len(fragile))

