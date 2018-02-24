from xlwt import *
from divres import *
import numpy as np


file = Workbook(encoding='utf-8')
table = file.add_sheet('Sheet1')

wd_array = np.array(wending)
cr_array = np.array(cuiruo)
jcr_array = np.array(jicuiruo)

#print(wd_array)
#print(cr_array)
#print(jcr_array)

row = 0
for index in range(len(wd_array)):
    table.write(row, 0, wd_array[index][0])
    table.write(row, 1, wd_array[index][1])
    row = row + 1

table.write(row, 0, 0)
row = row + 1

for index in range(len(cr_array)):
    table.write(row, 0, cr_array[index][0])
    table.write(row, 1, cr_array[index][1])
    row = row + 1

table.write(row, 0, 0)
row = row + 1

for index in range(len(jcr_array)):
    table.write(row, 0, jcr_array[index][0])
    table.write(row, 1, jcr_array[index][1])
    row = row + 1

file.save('Q:\\ariescc\\mcm\\icm\\resource\\finaldata\\mapdata.xlsx')

