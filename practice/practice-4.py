'''
@Description: code
@Author: MiCi
@Date: 2020-03-14 14:30:18
@LastEditTime: 2020-03-14 15:23:28
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np


class Practice4(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/US_Crime_Rates_1960_2014.csv'
        crimeData = pd.read_csv(path)
        # 预览尾5行
        print(crimeData.tail(5))

        # 查看数据类型
        print(crimeData.info())

        # 将Year的数据类型转换为datetime64
        crimeData['Year'] = pd.to_datetime(crimeData['Year'], format='%Y')
        print(crimeData.info())

        # 将Year设置为df的索引
        crimeData = crimeData.set_index('Year', drop=True)
        print(crimeData.head(5))

        # 删除Total列
        del crimeData['Total']
        print(crimeData.head())

        # 使用resample调整抽样，十年为一格
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
        # 由于population这一列不能直接取和，需要做一次修正
        crimeData2 = crimeData.resample('10AS').sum()
        print(crimeData2)
        populationData = crimeData['Population'].resample('10AS').max()
        crimeData2['Population'] = populationData
        print(crimeData2)

        # 返回每列值最大的年份
        print(crimeData.idxmax(0))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice4()
    example.exercise()
