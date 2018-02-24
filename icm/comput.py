import numpy as np
import pandas as pd
import xlrd
from pprint import pprint
from xlwt import *

"""
data2014.xls
"""

file = Workbook(encoding='utf-8')
table = file.add_sheet('sheet1')

data = pd.read_excel('./Resource/data2014.xlsx')
#data = pd.read_excel('./Resource/exceptEnvironment.xlsx')
#print(data.values.shape)
nrows, ncols = data.values.shape
#print(nrows, ncols)
array = np.array(data.values)
X0 = np.ones(4)

dij = np.array(data.values)

for row in range(nrows - 3):
    for col in range(1, ncols):
        array[row][col] = (array[row][col] - array[nrows-3][col]) / array[nrows-1][col]
        # 初始化 |xi(j)-x0(j)|
        dij[row][col] = abs(array[row][col] - 1)

#print(array[:-3, :][0])
#print(len(array))

#print(dij)
tmp = dij[:-3,1:]
#print(tmp)
# 求关联系数
a = tmp.min()
b = tmp.max()
p = 0.5
#print('a',a)
#print('b',b)

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
    xg_Z[col] = xg_Z[col] / (nrows-3)


xg_Z = xg_Z[1:]
#print(xg_Z)
xg_Z_sum = np.sum(xg_Z)

# 计算各项指标的权重
W = np.zeros(ncols)
for index in range(len(xg_Z)):
    W[index] = xg_Z[index] / xg_Z_sum

#print(W)


# 量化各个国家的发展水平
G = np.array(data.values[:nrows-3,:2])
for row in range(nrows - 3):
    G[row][1] = 0
    for col in range(1, ncols):
        G[row][1] = G[row][1] + (array[row][col]*W[col-1])
    # 1- G 为脆弱性
    G[row][1] = 1 - G[row][1]

print(G)

#for index in range(len(G)):
#    table.write(index, 0, G[index,0])
#    table.write(index, 1, G[index,1])

#file.save('Q:\\ariescc\\mcm\\out.xls')

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

