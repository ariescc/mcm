import xlrd
from xlwt import *
import numpy as np

file = Workbook(encoding = 'utf-8')

table = file.add_sheet('div')

workbook = xlrd.open_workbook('div_20.xls')
jmsheet = workbook.sheet_by_name('jm_sheet')
bcsheet = workbook.sheet_by_name('bc_sheet')
xzsheet = workbook.sheet_by_name('xz_sheet')

def write_div():
    table.write(0, 0, '小组序号')
    table.write(0, 1, '建模队员')
    table.write(0, 2, '编程队员')
    table.write(0, 3, '写作队员')
    for row in range(1, jmsheet.nrows):
        celjm = jmsheet.cell(row, 0)
        celbc = bcsheet.cell(row, 0)
        celxz = xzsheet.cell(row, 0)
        valjm = celjm.value
        valbc = celbc.value
        valxz = celxz.value
        table.write(row, 0, row)
        table.write(row, 1, valjm)
        table.write(row, 2, valbc + 40)
        table.write(row, 3, valxz + 80)

    file.save('Q:\\ariescc\\mcm\\mcm-one\\div_group.xls')

if __name__ == '__main__':
    write_div()
