import xlrd
import re
import numpy
from xlwt import *

file = Workbook(encoding = 'utf-8')

jmtable = file.add_sheet('jm_score')
bctable = file.add_sheet('bc_score')
xztable = file.add_sheet('xz_score')

workbook = xlrd.open_workbook('output.xls')
jmsheet = workbook.sheet_by_name('jm')
bcsheet = workbook.sheet_by_name('bc')
xzsheet = workbook.sheet_by_name('xz')

def read_xls_jm_sheet():
    p = list()
    for row in range(1, jmsheet.nrows):
        row_data = []
        for col in range(jmsheet.ncols):
            cel = jmsheet.cell(row, col)
            val = cel.value
            row_data.append(val)
        p.append(row_data)
    return p

def read_xls_bc_sheet():
    p = list()
    for row in range(1, bcsheet.nrows):
        row_data = []
        for col in range(bcsheet.ncols):
            cel = bcsheet.cell(row, col)
            val = cel.value
            row_data.append(val)
        p.append(row_data)
    return p

def read_xls_xz_sheet():
    p = list()
    for row in range(1, xzsheet.nrows):
        row_data = []
        for col in range(xzsheet.ncols):
            cel = xzsheet.cell(row, col)
            val = cel.value
            row_data.append(val)
        p.append(row_data)
    return p

def resolve_data_jm():
    data = read_xls_jm_sheet()
    score = list()
    for row in range(len(data)):
        tmp = 0
        for col in range(len(data[0])):
            if col >= 0 and col < 6:
                tmp += int(data[row][col])
            elif col == 6 or col == 8 or col == 10:
                tmp += 2 * int(data[row][col])
            elif col == 7 or col == 9 or col == 11:
                tmp += int(data[row][col])
        score.append(tmp)
    return score
    # print(len(score))

def resolve_data_bc():
    data = read_xls_bc_sheet()
    score = list()
    for row in range(len(data)):
        tmp = 0
        for col in range(len(data[0])):
            if col >= 0 and col < 6:
                tmp += int(data[row][col])
            elif col == 6 or col == 8 or col == 10:
                tmp += 2 * int(data[row][col])
            elif col == 7 or col == 9 or col == 11:
                tmp += int(data[row][col])
        score.append(tmp)
    return score
    # print(len(score))

def resolve_data_xz():
    data = read_xls_xz_sheet()
    score = list()
    for row in range(len(data)):
        tmp = 0
        for col in range(len(data[0])):
            if col >= 0 and col < 6:
                tmp += int(data[row][col])
            elif col == 6 or col == 8 or col == 10:
                tmp += 2 * int(data[row][col])
            elif col == 7 or col == 9 or col == 11:
                tmp += int(data[row][col])
        score.append(tmp)
    return score
    # print(len(score))

def update_scoreList():
    jmscore = list()
    jmscore = resolve_data_jm()
    jmtable.write(0, 0, 'stu_id')
    jmtable.write(0, 1, 'sum_score')
    for item in range(40):
        jmtable.write(item + 1, 0, item + 1)
        jmtable.write(item + 1, 1, jmscore[item])

    bcscore = list()
    bcscore = resolve_data_bc()
    bctable.write(0, 0, 'stu_id')
    bctable.write(0, 1, 'sum_score')
    for item in range(40):
        bctable.write(item + 1, 0, item + 1)
        bctable.write(item + 1, 1, bcscore[item])

    xzscore = list()
    xzscore = resolve_data_xz()
    xztable.write(0, 0, 'stu_id')
    xztable.write(0, 1, 'sum_score')
    for item in range(40):
        xztable.write(item + 1, 0, item + 1)
        xztable.write(item + 1, 1, xzscore[item])

    file.save('Q:\\ariescc\\mcm\\mcm-one\\sum_score.xls')

if __name__ == '__main__':
    update_scoreList()
    # resolve_data()