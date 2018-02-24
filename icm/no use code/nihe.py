import numpy as np
import pandas as pd
from xlwt import *


file = Workbook(encoding='utf-8')
table = file.add_sheet('Sheet1')

data = pd.read_excel('./resource/海拔5米.xls')
countries = pd.read_excel('./resource/data2014.xlsx')

data_array = np.array(data)
countries_array = np.array(countries)

nrows, ncols = countries.values.shape
rows, cols = data.values.shape
print(rows, cols)

res = list()
con = list()
for row in range(11, nrows):
    for ix in range(rows):
        if countries_array[row][0] == data_array[ix][0]:
            con.append(countries_array[row][0])
            res.append(data_array[ix][54])

for row in range(len(res)):
    table.write(row, 0, con[row])
    table.write(row, 1, res[row])

file.save('Q:\\ariescc\\mcm\\icm\\resource\\result.xls')


