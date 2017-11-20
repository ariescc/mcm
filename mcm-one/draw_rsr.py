import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

loandata = pd.DataFrame(pd.read_excel('rsr_group_res.xls'))

loandata = loandata.set_index('id')

loan_grade = loandata['rsr_value']

plt.rc('font', family = 'STXihei', size = 15)

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],loan_grade,color='#99CC01',alpha=0.8,align='center',edgecolor='white')

plt.xlabel('小组序号')
plt.ylabel('rsr')

plt.title('rsr 分布图')

plt.legend(['rsr'], loc = 'upper right')

plt.grid(color = '#95a5a6', linestyle = '--', linewidth = 1, axis = 'y', alpha = 0.4)

plt.xticks(a, ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))

plt.show()