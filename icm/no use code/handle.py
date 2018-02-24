import numpy as np
import pandas as pd
from xlwt import *

data = pd.read_excel('./resource/english/yeardata.xlsx')
nrows, ncols = data.values.shape
array = np.array(data.values)

file = Workbook(encoding='utf-8')
table = file.add_sheet('Sheet1')

for row in range(nrows):
    for col in range(ncols):
        table.write(col, row, array[row][col])

file.save('Q:\\ariescc\\mcm\\icm\\resource\\jiachang.xls')


