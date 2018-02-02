"""
**** 元胞自动机 ****

生命游戏模型（实现）

author: ariescc

"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 元胞矩阵维数
msize = 10

# init CA matrix of 10 × 10
ca_matrix = np.array(np.random.randint(0, 2, (msize, msize)))

# four directions
directions = [[0,-1],[-1,0],[1,0],[0,1]]

# 判断周围的元胞状态 => 此处使用摩尔领域,即上下左右
def judge_cell_state(x, y):
    cnt = 0
    for direction in directions:
        nx = x + direction[0]
        ny = y + direction[1]
        #print(nx, ny)
        if nx < msize and ny < msize and nx >= 0 and ny >=0 \
                and ca_matrix[nx][ny]:
            cnt += 1

    # amount of alive cell
    if cnt == 3:
        ca_matrix[x][y] = 1
    elif cnt == 2:
        pass
    else:
        ca_matrix[x][y] = 0


def run():
    last = [[]]
    curr = ca_matrix
    while True:
        if np.all(last == curr):
            break
        last = np.copy(curr)
        for i in range(msize):
            for j in range(msize):
                judge_cell_state(i, j)

        curr = np.copy(ca_matrix)
        print(ca_matrix)
        print('---------------------')

    # 绘制图片
    for i in range(msize):
        for j in range(msize):
            if curr[i][j]:
                curr[i][j] = 0
            else:
                curr[i][j] = 255

    image = Image.fromarray(curr)
    Image._show(image)

    print('over')


if __name__ == '__main__':
    print('***********************')
    print(ca_matrix)
    print('***********************')
    #print(judge_cell_state(4, 4))
    run()
    #print(np.all(bb))



