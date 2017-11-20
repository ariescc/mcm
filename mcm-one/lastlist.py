import xlrd
import numpy
from xlwt import *

file = Workbook(encoding = 'utf-8')

listsheet = file.add_sheet('最终名单')

workbookrsr = xlrd.open_workbook('rsr_input.xls')
workbookgroup = xlrd.open_workbook('div_group.xls')

rsrsheet = workbookrsr.sheet_by_name('rsr')
groupsheet = workbookgroup.sheet_by_name('div')

def build_list():
    listsheet.write(0, 0, '小组序号')
    listsheet.write(0, 1, '建模队员')
    listsheet.write(0, 2, '编程队员')
    listsheet.write(0, 3, '写作队员')
    for row in range(1, rsrsheet.nrows):
        aa = rsrsheet.cell(row, 0)
        celaa = aa.value
        tem = celaa
        print(tem)
        flag = 0
        for item in range(1, groupsheet.nrows):
            bb = groupsheet.cell(item, 0)
            celbb = bb.value
            cur = int(celbb)
            if tem == cur:
                flag = 1
                for col in range(groupsheet.ncols):
                    cel = groupsheet.cell(item, col)
                    val = cel.value
                    # print(val)
                    listsheet.write(row, col, val)
            if flag == 1:
                break
    
    file.save('Q:\\ariescc\\mcm\\mcm-one\\final_list.xls')

if __name__ == '__main__':
    build_list()