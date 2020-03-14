'''
@Description: code
@Author: MiCi
@Date: 2020-03-14 08:46:33
@LastEditTime: 2020-03-14 14:28:18
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np


class Basic5(object):

    def __init__(self):
        return

    def basic_use(self):
        df = pd.DataFrame(np.random.rand(10, 5), columns=list('ABCDE'))
        # describe描述性统计
        print(df.describe())

        # mean计算每一列平均值
        print(df.mean())

        # corr得到df每一列与其他列相关系数
        print(df.corr())

        # count得到df每一列的非空计数
        print(df.count())

        # max得到df每一列最大值
        print(df.max())

        # min得到df每一列最小值
        print(df.min())

        # median得到df每一列的中位数
        print(df.median())

        # std得到df每一列标准差
        print(df.std())

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic5()
    example.basic_use()
