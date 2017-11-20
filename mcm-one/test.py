import random
from xlwt import *

# excel
file = Workbook(encoding = 'utf-8')

tablea = file.add_sheet('jm',cell_overwrite_ok=True)
tableb = file.add_sheet('bc',cell_overwrite_ok=True)
tablec = file.add_sheet('xz',cell_overwrite_ok=True)

# 获取一个人的成绩
def get_score():
    score = ""
    jma = random.randint(70, 100)
    jmb = random.randint(70, 100)
    bca = random.randint(70, 100)
    bcb = random.randint(70, 100)
    xza = random.randint(70, 100)
    xzb = random.randint(70, 100)

    jmca = random.randint(0, 4)
    jmcb = random.randint(0, 4)
    bcca = random.randint(0, 4)
    bccb = random.randint(0, 4)
    xzca = random.randint(0, 4)
    xzcb = random.randint(0, 4)
    score = str(jma) + " " + str(jmb) + " " + str(bca) + " " + str(bcb) + " " + str(xza) + " " + str(xzb) + " " + str(jmca) + " " + str(jmcb) + " " + str(bcca) + " " + str(bccb) + " " + str(xzca) + " " + str(xzcb)
    return score

# 120人成绩生成
def scoreList():
    sheet = ['高等数学', '线性代数', 'C++程序设计', '数据结构', '大学英语1', '大学英语2', '国家数模比赛', '校数模比赛', '国家编程比赛', '校编程比赛', '国家英语比赛', '校英语比赛']
    for item in range(12):
        tablea.write(0, item, sheet[item])
    for jm in range(1, 41):
        tmp = get_score()
        sp = list()
        sp = tmp.split(" ")
        # tablea.write(jm, 0, jm)
        if jm % 10 == 1 or jm % 10 == 5 or jm % 10 == 8:
            for col in range(12):
                if col == 0 or col == 1 or col == 4 or col == 6 or col == 7 or col == 11:
                    tablea.write(jm, col, sp[col])
                else:
                    tablea.write(jm, col, 0)
        if jm % 10 == 9 or jm % 10 == 3 or jm % 10 == 7:
            for col in range(12):
                if col == 0 or col == 1 or col == 3 or col == 6 or col == 7 or col == 9:
                    tablea.write(jm, col, sp[col])
                else:
                    tablea.write(jm, col, 0)
        if jm % 10 == 2 or jm % 10 == 4 or jm % 10 == 0 or jm % 10 == 6:
            for col in range(12):
                if col == 1 or col == 2 or col == 5 or col == 7 or col == 8 or col == 10:
                    tablea.write(jm, col, sp[col])
                else:
                    tablea.write(jm, col, 0)

    for item in range(12):
        tableb.write(0, item, sheet[item])
    for bc in range(1, 41):
        tmp = get_score()
        sp = list()
        sp = tmp.split(" ")
        # tableb.write(jm, 0, jm)
        if bc % 10 == 1 or bc % 10 == 5 or bc % 10 == 8:
            for col in range(12):
                if col == 2 or col == 3 or col == 4 or col == 8 or col == 9 or col == 10:
                    tableb.write(bc, col, sp[col])
                else:
                    tableb.write(bc, col, 0)
        if bc % 10 == 9 or bc % 10 == 3 or bc % 10 == 7:
            for col in range(12):
                if col == 2 or col == 3 or col == 0 or col == 8 or col == 9 or col == 7:
                    tableb.write(bc, col, sp[col])
                else:
                    tableb.write(bc, col, 0)
        if bc % 10 == 2 or bc % 10 == 4 or bc % 10 == 0 or bc % 10 == 6:
            for col in range(12):
                if col == 0 or col == 3 or col == 5 or col == 7 or col == 8 or col == 11:
                    tableb.write(bc, col, sp[col])
                else:
                    tableb.write(bc, col, 0)

    for item in range(12):
        tablec.write(0, item, sheet[item])
    for xz in range(1, 41):
        tmp = get_score()
        sp = list()
        sp = tmp.split(" ")
        # tablec.write(jm, 0, jm)
        if xz % 10 == 1 or xz % 10 == 5 or xz % 10 == 8:
            for col in range(12):
                if col == 4 or col == 5 or col == 1 or col == 10 or col == 11 or col == 6:
                    tablec.write(xz, col, sp[col])
                else:
                    tablec.write(xz, col, 0)
        if xz % 10 == 9 or xz % 10 == 3 or xz % 10 == 7:
            for col in range(12):
                if col == 4 or col == 5 or col == 3 or col == 10 or col == 11 or col == 9:
                    tablec.write(xz, col, sp[col])
                else:
                    tablec.write(xz, col, 0)
        if xz % 10 == 2 or xz % 10 == 4 or xz % 10 == 0 or xz % 10 == 6 or col == 7 or col == 8 or col == 10:
            for col in range(12):
                if col == 0 or col == 2 or col == 4:
                    tablec.write(xz, col, sp[col])
                else:
                    tablec.write(xz, col, 0)

    file.save('Q:\\ariescc\\mcm\\mcm-one\\output.xls')

if __name__ == '__main__':
    scoreList()