import xlrd
import re
import numpy
from xlwt import *

file = Workbook(encoding = 'utf-8')

table = file.add_sheet('sheet1')


def read_xls():
    workbook = xlrd.open_workbook('output.xls')
    booksheet = workbook.sheet_by_name('aaa')
    p = list()
    for row in range(1, booksheet.nrows):
        row_data = []
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            row_data.append(val)
        p.append(row_data)
    return p

def resolve_data():
    data = read_xls()
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
    score = list()
    score = resolve_data()
    table.write(0, 0, 'stu_id')
    table.write(0, 1, 'sum_score')
    for item in range(120):
        table.write(item + 1, 0, item + 1)
        table.write(item + 1, 1, score[item])
    file.save('Q:\\mcm\\sum_score.xls')

if __name__ == '__main__':
    update_scoreList()
    # resolve_data()