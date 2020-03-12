'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 15:04:12
@LastEditTime: 2020-03-12 21:47:10
@LastEditors: MiCi
'''

import pandas as pd


class Practice2(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/Euro2012_stats.csv'

        euroData = pd.read_csv(path)
        print(euroData)

        # 读取DataFrame信息
        print(euroData.info())

        # 多少支球队
        print('Team Counts:', euroData.shape[0])

        # 抽取Team、Yellow Cards、Red Cards作为单独DataFrame
        cardData = euroData[['Team', 'Yellow Cards', 'Red Cards']]
        print(cardData)

        # 按照先红牌再黄牌排序
        print(cardData.sort_values(
            ['Red Cards', 'Yellow Cards'], ascending=False))

        # 平均黄牌数量
        print('Avg Yellow Cards Counts:', cardData['Yellow Cards'].mean())

        # 进球数Goals超过6的队伍
        print(euroData[euroData['Goals'] > 6])

        # 选取球队名称为’G‘开头
        print(euroData[euroData['Team'].str.startswith('G')])

        # iloc类似list索引,[行切片，列切片]，选取前3行，前7列数据
        print(euroData.iloc[0:2, 0:7])
        # 选取1、3、5列
        print(euroData.iloc[0:2, [0, 2, 4]])

        # isin判断是否在，选取England、Italy两支队伍，Team+Shooting Accuracy
        print(euroData.loc[euroData.Team.isin(
            ['England', 'Italy']), ['Team', 'Shooting Accuracy']])

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice2()
    example.exercise()
