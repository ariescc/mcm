import xlrd

workbook = xlrd.open_workbook('data.xls')

sheet = workbook.sheet_by_name('Sheet1')

def split_number(line):
    sp = line.split(',')
    return sp

def create_dict():
    dic = dict()
    dic = {}
    for row in range(1, sheet.nrows):
        cel_0 = sheet.cell(row, 0)
        val_0 = str(int(cel_0.value))
        cel_1 = sheet.cell(row, 1)
        val_1 = cel_1.value
        splist = split_number(val_1)
        dic[val_0] = splist
    return dic

# 判断是否覆盖全
def judge_vis_over(line):
    for item in range(45):
        if line[item] == 0:
            return False
    return True

def solve_qus():
    # 标记所有控件均未被遍历到
    vis = list()
    for item in range(45):
        vis.append(0)

    dicc = create_dict()

    minium = 100
    cnt = 0

    res = list()

    for x in range(1, sheet.nrows):
        cnt = 0
        for y in range(x, sheet.nrows):
            index = str(y)
            cur_list = dicc[index]
            sp = cur_list[0].split('，')
            for item in range(len(sp)):
                if sp[item] != '':
                    vis[int(sp[item])-1] = 1
                else:
                    pass
            if judge_vis_over(vis) == True:
                for vis_index in range(45):
                    vis[vis_index] = 0
                res.append(cnt)
                break
            else:
                cnt += 1

    minium = 100

    for res_index in range(len(res)):
        if res[res_index] < minium:
            minium = res[res_index]

    return minium


if __name__ == '__main__':
    print(solve_qus())
