"""
**** 元胞自动机 ****

生命游戏模型（实现）

author: ariescc

"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


msize = 5

# init CA matrix of 10 × 10
ca_matrix = np.array(np.random.randint(0, 2, (msize, msize)))

bb = [[1 ,1],[1,1]]

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
        ca_matrix[x][y] = 0
    elif cnt == 2:
        pass
    else:
        ca_matrix[x][y] = 1


def run():
    while True:
        for i in range(msize):
            for j in range(msize):
                judge_cell_state(i, j)

        print(ca_matrix)
        print('---------------------')

        #image = Image.fromarray(ca_matrix)
        #Image._show(image)

        if np.all(ca_matrix) == True:
            break
    print('over')


if __name__ == '__main__':
    print('初始数组')
    print(ca_matrix)
    print('***********************')
    #print(ca_matrix)
    #print(judge_cell_state(4, 4))
    run()
    #print(np.all(bb))



