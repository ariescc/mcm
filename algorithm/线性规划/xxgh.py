"""
线性规划

文档: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog


函数原型：
    scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None,
                            bounds=None, method='simplex', callback=None, options=None)

"""

import numpy as np
from scipy.optimize import linprog


# 目标函数系数 (矩阵)
c = np.array([4, 3])

# 约束条件系数(矩阵)

A_ub = np.array([[2, 1],
                 [1, 1]])

# 约束条件上界(矩阵)
b_ub = np.array([10, 8])

# 定义变量边界范围(x1, x2 ...)
bounds = ((0, None), (0, 7))

options = {"disp": True}

# c 正序求最小值， -c求最大值

min_res = linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
max_res = linprog(c=-c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)

print(min_res)
print('------------------------')
print(max_res)

