import xlrd
from xlwt import *
import numpy as np

file = Workbook(encoding = 'utf-8')
table = file.add_sheet('Sheet1')

workbook = xlrd.open_workbook('data.xls')

sheet = workbook.sheet_by_name('Sheet1')

def read_data():
    # 初始化 45 * 35 的全1 矩阵
    mark = np.zeros([45, 35], dtype=np.int16)

    for row in range(1, sheet.nrows):
        # 解析得到所有的 第 i 个部件是否由第 j 条指令控制
        cel = sheet.cell(row, 1)
        val = cel.value
        sp = val.split('，')
        # print(sp[0])
        # print(sp)
        for item in range(len(sp)):
            col = int(sp[item])
            mark[col-1][row-1] = -1

    return mark

def print_result():
    arr = read_data()
    with open('output.txt', 'w', encoding = 'utf-8') as fil:
        tmp = ''
        for row in range(45):
            for col in range(35):
                if col == 34:
                    tmp += str(arr[row][col]) + ';' + '\n'
                else:
                    tmp += str(arr[row][col]) + ','
        fil.write(tmp)

def build_F1_array():
    F1Array = np.ones(35, dtype=np.int16)
    with open('F1_array.txt', 'w', encoding = 'utf-8') as fil:
        tmp = ''
        for item in range(35):
            tmp += str(F1Array[item]) + ','
        fil.write(tmp)

def build_F2_array():
    F2Array = np.ones(45, dtype=np.int16)
    with open('F2_array.txt', 'w', encoding = 'utf-8') as fil:
        tmp = ''
        for item in range(45):
            tmp += str(-F2Array[item]) + ','
        fil.write(tmp)

def build_length_array():
    tmp = ''
    for row in range(1, sheet.nrows):
        # 读取每个指令的长度
        cel = sheet.cell(row, 2)
        val = cel.value
        tmp += str(int(val)) + ','

    with open('length_array.txt', 'w', encoding = 'utf-8') as fil:
        fil.write(tmp)

def build_intcon_array():
    tmp = ''
    for item in range(1, 36):
        tmp += str(item) + ','
    
    with open('intcon_array.txt', 'w', encoding = 'utf-8') as fil:
        fil.write(tmp)

if __name__ == '__main__':
    # print_result()
    # read_data()
    # build_F1_array()
    # build_F2_array()
    # build_length_array()
    build_intcon_array()