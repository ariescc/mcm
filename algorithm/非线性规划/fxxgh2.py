"""
求解非线性规划

    5*x1 + 3 = 0
    5 * x0**2 - 2*sin(x1*x2) = 0
    x1 * x2 - 1.5 = 0
"""

import numpy as np
from scipy.optimize import fsolve


def func(x):
    x0, x1, x2 = x.tolist()
    return [
        5*x1 + 3,
        5 * x0**2 - 2*np.sin(x1*x2),
        x1 * x2 - 1.5
    ]

# 求雅克比矩阵（对每个式子的x0, x1, x2求偏导
def fpr(x):
    x0, x1, x2 = x.tolist()
    return [
        [0, 5, 0],
        [10*x0, -2*x2*np.cos(x1*x2), -2*x1*np.cos(x1*x2)],
        [0, x2, x1]
    ]

if __name__ == '__main__':
    #res = fsolve(func, [1, 1, 1])
    res = fsolve(func, [1, 1, 1], fprime=fpr) # 传入雅克比矩阵可以提高4倍计算效率
    print(res)

