import random
from xlwt import *

# excel
file = Workbook(encoding = 'utf-8')

table = file.add_sheet('aaa',cell_overwrite_ok=True)

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
        table.write(0, item, sheet[item])
    for jm in range(1, 41):
        tmp = get_score()
        sp = list()
        sp = tmp.split(" ")
        # table.write(jm, 0, jm)
        if jm % 10 == 1 or jm % 10 == 5 or jm % 10 == 8:
            for col in range(12):
                if col == 0 or col == 1 or col == 4 or col == 6 or col == 7 or col == 11:
                    table.write(jm, col, sp[col])
                else:
                    table.write(jm, col, 0)
        if jm % 10 == 9 or jm % 10 == 3 or jm % 10 == 7:
            for col in range(12):
                if col == 0 or col == 1 or col == 3 or col == 6 or col == 7 or col == 9:
                    table.write(jm, col, sp[col])
                else:
                    table.write(jm, col, 0)
        if jm % 10 == 2 or jm % 10 == 4 or jm % 10 == 0 or jm % 10 == 6:
            for col in range(12):
                if col == 1 or col == 2 or col == 5 or col == 7 or col == 8 or col == 10:
                    table.write(jm, col, sp[col])
                else:
                    table.write(jm, col, 0)

    for bc in range(41, 81):
        tmp = get_score()
        sp = list()
        sp = tmp.split(" ")
        # table.write(jm, 0, jm)
        if bc % 10 == 1 or bc % 10 == 5 or bc % 10 == 8:
            for col in range(12):
                if col == 2 or col == 3 or col == 4 or col == 8 or col == 9 or col == 10:
                    table.write(bc, col, sp[col])
                else:
                    table.write(bc, col, 0)
        if bc % 10 == 9 or bc % 10 == 3 or bc % 10 == 7:
            for col in range(12):
                if col == 2 or col == 3 or col == 0 or col == 8 or col == 9 or col == 7:
                    table.write(bc, col, sp[col])
                else:
                    table.write(bc, col, 0)
        if bc % 10 == 2 or bc % 10 == 4 or bc % 10 == 0 or bc % 10 == 6:
            for col in range(12):
                if col == 0 or col == 3 or col == 5 or col == 7 or col == 8 or col == 11:
                    table.write(bc, col, sp[col])
                else:
                    table.write(bc, col, 0)

    for xz in range(81, 121):
        tmp = get_score()
        sp = list()
        sp = tmp.split(" ")
        # table.write(jm, 0, jm)
        if xz % 10 == 1 or xz % 10 == 5 or xz % 10 == 8:
            for col in range(12):
                if col == 4 or col == 5 or col == 1 or col == 10 or col == 11 or col == 6:
                    table.write(xz, col, sp[col])
                else:
                    table.write(xz, col, 0)
        if xz % 10 == 9 or xz % 10 == 3 or xz % 10 == 7:
            for col in range(12):
                if col == 4 or col == 5 or col == 3 or col == 10 or col == 11 or col == 9:
                    table.write(xz, col, sp[col])
                else:
                    table.write(xz, col, 0)
        if xz % 10 == 2 or xz % 10 == 4 or xz % 10 == 0 or xz % 10 == 6 or col == 7 or col == 8 or col == 10:
            for col in range(12):
                if col == 0 or col == 2 or col == 4:
                    table.write(xz, col, sp[col])
                else:
                    table.write(xz, col, 0)

    file.save('Q:\\mcm\\output.xls')

if __name__ == '__main__':
    scoreList()