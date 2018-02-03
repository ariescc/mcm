import numpy as np
import matplotlib.pyplot as plt


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

X = ['阿根廷', '亚美尼亚', '澳大利亚', '阿塞拜疆', '比利时', '保加利亚', '白俄罗斯', '巴西', '博茨瓦纳', '加拿大']
Y = [0.34907581451644099, 0.28976857860299399, 0.57396702931141019, 0.41924887132432448, 0.53632288155511376, 0.36975553614783396, 0.41938632529574055, 0.4987781460848873, 0.24604314628276353, 0.65176053910203235]
# 设置字体倾斜
plt.xticks(rotation=45)

plt.bar(X, Y, color='DarkBlue')
plt.show()

