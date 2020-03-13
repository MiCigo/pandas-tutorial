'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 15:04:12
@LastEditTime: 2020-03-13 11:27:07
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np


class Basic2(object):

    def __init__(self):
        return

    def basic_use(self):
        df = pd.DataFrame({'A': np.array([1, np.nan, 2, 3, 6, np.nan]),
                           'B': np.array([np.nan, 4, np.nan, 5, 9, np.nan]),
                           'C': 'test'})
        # 重命名列名
        df.columns = ['a', 'b', 'c']
        print(df)

        # 检查df中为null的情况
        print(pd.isnull(df))

        # 检查df中不为null的情况
        print(pd.notnull(df))

        # dropna移除df中包含null的行
        # axis=1为列
        # how=‘all’移除全部为空
        # thresh=n 保留至少有n个非null数据的行
        # print(df.dropna())
        # print(df.dropna(axis=1))

        # fillna(x)将df中所有控制替换为x
        print(df.fillna('hah'))

        # 全列重命名
        # print(df.rename(columns=lambda x: x+2))

        # 选择部分列重名名
        print(df.rename(columns={'A': 'newA', 'B': 'newB'}))

        # 设置索引
        print(df.set_index('NewIndex'))

        # 改变全体索引
        print(df.rename(index=lambda x: x+1))

        testSeries = pd.Series([1, 3, 5, np.nan, 7, 9, 9])
        # astype 转换格式
        print(testSeries.astype(float))

        # Series替换
        print(testSeries.replace(1, 'one'))

        # Series多个替换
        print(testSeries.replace([1, 3], ['one', 'three']))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic2()
    example.basic_use()
