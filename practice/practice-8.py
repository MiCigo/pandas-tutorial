'''
@Description: code
@Author: MiCi
@Date: 2020-03-15 21:31:58
@LastEditTime: 2020-03-15 21:58:24
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Practice8(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/Apple_stock.csv'
        appleData = pd.read_csv(path)
        print(appleData.head(5))
        print(appleData.dtypes)

        # 将Date转化为datetime类型，并设置为索引
        appleData['Date'] = pd.to_datetime(appleData['Date'])
        appleData = appleData.set_index('Date')
        print(appleData.head(5))

        # 判定是否有重复日期
        print(appleData.index.is_unique)

        # 设置index为升序
        print(appleData.sort_index(ascending=True).head())

        # 最早的日期与最晚的日期间隔
        print((appleData.index.max() - appleData.index.min()).days)

        # 一共有多少个月
        appleMth = appleData.resample('BM').mean()
        print(len(appleMth.index))

        # 时序图Adj Close
        appleY = appleData['Adj Close']
        appleX = appleData.index
        plt.plot(appleX, appleY)
        plt.show()

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice8()
    example.exercise()
