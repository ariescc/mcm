import numpy as np
import pandas as pd
import xlrd
from pprint import pprint


"""
cli气候变化量
"""
data = pd.read_excel('./resource/clidata.xlsx')
nrows, ncols = data.values.shape
#print(nrows, ncols)

array = np.array(data.values)
dij = np.array(data.values)

for row in range(nrows - 3):
    for col in range(1, ncols):
        array[row][col] = (array[row][col] - array[nrows-3][col]) / array[nrows-1][col]
        dij[row][col] = abs(array[row][col] - 1)

#print(array[:-3, :])

tmp = dij[:-3, 1:]
# 求关联系数
a = tmp.min()
b = tmp.max()
p = 0.5

print('a',a)
print('b',b)

print('***********************')

xg_y = np.array(data.values)
for row in range(nrows-3):
    for col in range(1, ncols):
        xg_y[row][col] = (a + b*p) / (dij[row][col] + b*p)

# 国家中各项指标的平均关联系数
xg_Z = np.zeros(ncols)
for col in range(1, ncols):
    for row in range(nrows-3):
        xg_Z[col] = xg_Z[col] + xg_y[row][col]
    xg_Z[col] = xg_Z[col] / (nrows-3)

xg_Z = xg_Z[1:]
xg_Z_sum = np.sum(xg_Z)

# 计算各项指标的权重
W = np.zeros(ncols)
for index in range(len(xg_Z)):
    W[index] = xg_Z[index] / xg_Z_sum

#print(W)

# 求气候变化量
cli = list()
for row in range(nrows-3):
    tp = 0
    for col in range(1, ncols-1):
        tp = tp + float(array[row][col])*W[col-1]
    cli.append(tp)

print(cli)

