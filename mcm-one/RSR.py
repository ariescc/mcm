import xlrd
import numpy
from xlwt import *

file = Workbook(encoding = 'utf-8')

rsrtable = file.add_sheet('rsr')

workbook = xlrd.open_workbook('RSR_group.xls')
divsheet = workbook.sheet_by_name('div')

def cal_rsr():

    rsrtable.write(0, 0, '小组序号')
    rsrtable.write(0, 1, 'rsr_value')

    for row in range(1, divsheet.nrows):
        tmp = 0
        for col in range(4, divsheet.ncols):
            cel = divsheet.cell(row, col)
            val = cel.value
            tmp += int(val)
        rsrtable.write(row, 0, row)
        rsrtable.write(row, 1, tmp / 140)
    
    file.save('Q:\\ariescc\\mcm\\mcm-one\\rsr_group_res.xls')

if __name__ == '__main__':
    cal_rsr()