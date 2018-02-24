import xlrd
from xlwt import *

file = Workbook(encoding='utf-8')
table = file.add_sheet('Sheet1')

workbook = xlrd.open_workbook('./resource/engdata.xls')
sheet = workbook.sheet_by_name('Data')

for row in range(3, sheet.nrows):
    celname = sheet.cell(row, 0)
    celdescription = sheet.cell(row, 2)
    valname = celname.value
    valdescription = celdescription.value
    table.write(row, 0, valname)
    table.write(row, 1, valdescription)

for row in range(3, sheet.nrows):
    cel08 = sheet.cell(row, sheet.ncols-10)
    cel09 = sheet.cell(row, sheet.ncols-9)
    cel10 = sheet.cell(row, sheet.ncols-8)
    cel11 = sheet.cell(row, sheet.ncols-7)
    cel12 = sheet.cell(row, sheet.ncols-6)
    cel13 = sheet.cell(row, sheet.ncols-5)
    cel14 = sheet.cell(row, sheet.ncols-4)
    cel15 = sheet.cell(row, sheet.ncols-3)
    cel16 = sheet.cell(row, sheet.ncols-2)
    cel17 = sheet.cell(row, sheet.ncols-1)
    val08 = cel08.value
    val09 = cel09.value
    val10 = cel10.value
    val11 = cel11.value
    val12 = cel12.value
    val13 = cel13.value
    val14 = cel14.value
    val15 = cel15.value
    val16 = cel16.value
    val17 = cel17.value
    table.write(row, 2, val08)
    table.write(row, 3, val09)
    table.write(row, 4, val10)
    table.write(row, 5, val11)
    table.write(row, 6, val12)
    table.write(row, 7, val13)
    table.write(row, 8, val14)
    table.write(row, 9, val15)
    table.write(row, 10, val16)
    table.write(row, 11, val17)


file.save('Q:\\ariescc\\mcm\\icm\\resource\\ed.xls')

