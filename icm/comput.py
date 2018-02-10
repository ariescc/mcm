import numpy as np
import pandas as pd
import xlrd
from pprint import pprint

"""
data.xls
国家  出生率  死亡率  GDP总额  人均GDP
"""

data = pd.read_excel('./Resource/data2014.xlsx')
#print(data.values.shape)
nrows, ncols = data.values.shape
array = np.array(data.values)
X0 = np.ones(4)

dij = np.array(data.values)

for row in range(nrows - 3):
    for col in range(1, ncols):
        array[row][col] = (array[row][col] - array[10][col]) / array[12][col]
        # 初始化 |xi(j)-x0(j)|
        dij[row][col] = abs(array[row][col] - 1)

#print(array[:-3, :])
#print(len(array))

#print(dij)
tmp = dij[:-3,1:]
#print(tmp)
# 求关联系数
a = tmp.min()
b = tmp.max()
p = 0.5
print(a)
print(b)

xg_y = np.array(data.values)
for row in range(nrows - 3):
    for col in range(1, ncols):
        xg_y[row][col] = (a + b*p) / (dij[row][col] + b*p)

#print(xg_y)
# 国家中各项指标的平均关联系数
xg_Z = np.zeros(ncols)

for col in range(1, ncols):
    for row in range(nrows - 3):
        xg_Z[col] = xg_Z[col] + xg_y[row][col]
    xg_Z[col] = xg_Z[col] / 10


xg_Z = xg_Z[1:]
#print(xg_Z)
xg_Z_sum = np.sum(xg_Z)

# 计算各项指标的权重
W = np.zeros(ncols)
for index in range(len(xg_Z)):
    W[index] = xg_Z[index] / xg_Z_sum

print(W)


# 量化各个国家的发展水平
G = np.array(data.values[:nrows-3,:2])
for row in range(nrows - 3):
    G[row][1] = 0
    for col in range(1, ncols):
        G[row][1] = G[row][1] + (array[row][col]*W[col-1])
    # 1- G 为脆弱性
    G[row][1] = 1 - G[row][1]

print(G)


#fragile = list()
# 1 - G 为各国的脆弱性水平
#for index in range(len(G)):
#    dic = dict()
#    dic[G[index][0]] = 1 - G[index][1]
#    fragile.append(dic)

#print(fragile)
#name = list()
#value = list()
#for row in range(nrows-3):
#    name.append(G[row][0])
#    value.append(G[row][1])

#print(name)
#print(value)

