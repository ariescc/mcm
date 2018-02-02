"""
求定积分

    x**2 + y**2 = 1
    上半圆积分

二重积分： dblquad
三重积分： tplquad
"""

import numpy as np
from scipy import integrate


def func(x):
    return np.sqrt(1 - x**2)

if __name__ == '__main__':
    #res, err = integrate.quad(func, -1, 1)
    res, err = integrate.quad(lambda x:np.sqrt(1-x**2), -1, 1)
    print(res)

