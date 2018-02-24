"""
计算去除指标前后脆弱性量化差值
"""
from fragile import fragile
from exceptFragile import exceptFragile
import numpy as np


old_fragile = np.array(fragile)
new_fragile = np.array(exceptFragile)

#print(old_fragile)
#print(new_fragile)
Dfragile = np.copy(old_fragile)
for index in range(len(fragile)):
    Dfragile[index][1] = float(old_fragile[index][1]) - float(new_fragile[index][1])

print(Dfragile)

