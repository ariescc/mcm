import pandas as pd
from pandas import DataFrame
import numpy as np

def sort_excel():
    lc = pd.DataFrame(pd.read_excel('Q:\\mcm\\sum_score.xls'))

    print(lc)

    lc.sort_values(by = 'sum_score', ascending = False)

    # print(lc.head(3))

if __name__ == '__main__':
    sort_excel()