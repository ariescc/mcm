"""
非线性规划

求解非线性方程：

    5*x1 - 25 = 0
    5*x0**2 - x1*x2 = 0
    x2*x0 - 27 = 0
"""

import numpy as np
from scipy.optimize import fsolve


def func(x):
    x0, x1, x2 = x.tolist()
    return [
        5*x1 - 25,
        5*x0**2 - x1*x2,
        x2*x0 - 27
    ]


if __name__ == '__main__':
    res = fsolve(func, [3, 3, 3])
    print(res)

