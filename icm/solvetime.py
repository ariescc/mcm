import numpy as np
import pandas as pd


data = pd.read_excel('./resource/10yeardata.xlsx')
#print(data)

array = np.array(data.values)
#print(array)

f_array = list()
for index in range(len(array)):
    f_array.append(array[index][1])

# 初始f0
f_array = np.array(f_array)
#print(len(f_array))

# 一次累加f1
f1_array = np.cumsum(f_array)
#print(len(f1_array), 'sdf')

g_array = list()
for index in range(len(f1_array)-1):
    g_array.append((f1_array[index] + f1_array[index + 1])/2)

#print(len(g_array), 'asdf')

B_array = list()
for index in range(len(g_array)):
    tmp = list()
    tmp.append(-g_array[index])
    tmp.append(1)
    B_array.append(tmp)

B_array = np.array(B_array)
#print(len(B_array))

Y_array = list()
for index in range(1, len(f_array)):
    Y_array.append(f_array[index])

Y_array = np.array(Y_array)[np.newaxis,].T
#print(Y_array.shape)

arr = np.mat(np.dot(B_array.T, B_array)).I
arr = np.dot(arr, B_array.T)
a, b = np.dot(arr, Y_array)
#print(a[0,0], b[0,0])

ba = b[0,0] / a[0,0]
f1_array[0] = f_array[0]
#print(f1_array[0])

f1x_array = list()
f1x_array.append(f1_array[0])
for index in range(18):
    f1x_array.append((f1_array[0]-ba)*np.exp(-a[0,0]*index) + ba)

#print(f1x_array)

f0x_array = list()
f0x_array.append(f_array[0])
for index in range(1, 19):
#    print(index)
    f0x_array.append(f1x_array[index]-f1x_array[index-1])

print(f0x_array)

# 检验精度
dx0_array = list()
dx_array = list()
for index in range(8):
    dx0_array.append(f_array[index]-f0x_array[index])

for index in range(8):
    dx_array.append(abs(dx0_array[index]/f_array[index]))

res = 0
for index in range(8):
    res = res + dx_array[index]

dx = res / 9
#print(dx)

