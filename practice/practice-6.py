'''
@Description: code
@Author: MiCi
@Date: 2020-03-14 20:52:51
@LastEditTime: 2020-03-14 21:37:25
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np
import datetime


class Practice6(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/wind.data'
        windData = pd.read_table(path, sep='\s+', parse_dates=[[0, 1, 2]])
        print(windData.head(10))

        def fix_year(x):
            year = x.year - 100 if x.year > 1989 else x.year
            return datetime.date(year, x.month, x.day)
        windData['Yr_Mo_Dy'] = windData['Yr_Mo_Dy'].apply(fix_year)
        print(windData.head(10))

        # 设置日期为索引
        windData['Yr_Mo_Dy'] = pd.to_datetime(windData['Yr_Mo_Dy'])
        windData = windData.set_index('Yr_Mo_Dy')
        print(windData.head(10))

        # 统计每一列有多少缺失数据
        print(windData.isnull().sum())

        # 统计每一列有多少完整数据
        print((windData.shape[0] - windData.isnull().sum()))

        # 统计每一列的平均值
        print(windData.mean())

        # 统计整体平均值
        print(windData.mean().mean())

        # 创建一个locStatsData存储每个地方风速最小、最大、平均、标准差
        locStatsData = pd.DataFrame()
        locStatsData['min'] = windData.min()
        locStatsData['max'] = windData.max()
        locStatsData['mean'] = windData.mean()
        locStatsData['std'] = windData.std()
        print(locStatsData.head(10))

        # 创建一个dayStats存储每天风速最小、最大、平均、标准差
        dayStatsData = pd.DataFrame()
        dayStatsData['min'] = windData.min(axis=1)
        dayStatsData['max'] = windData.max(axis=1)
        dayStatsData['mean'] = windData.mean(axis=1)
        dayStatsData['std'] = windData.std(axis=1)
        print(dayStatsData.head(10))

        # 计算每一个地方一月份的平均风速
        windData['date'] = windData.index
        windData['month'] = windData['date'].apply(lambda date: date.month)
        januaryWinds = windData.query('month == 1')
        print(januaryWinds.mean())

        # 对数据按照年为频率抽样
        windData['day'] = windData['date'].apply(lambda date: date.day)
        print(windData.query('month == 1 and day == 1'))

        # 对数据按照月为频率抽样
        print(windData.query('day == 1').head(10))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice6()
    example.exercise()
