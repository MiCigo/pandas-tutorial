'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 21:11:37
@LastEditTime: 2020-03-12 22:39:23
@LastEditors: MiCi
'''

import pandas as pd


class Practice3(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/drinks.csv'
        drinksData = pd.read_csv(path)
        print(drinksData.head(10))

        # 哪个continent平均消耗beer最高
        print('Avg Beer:\n', drinksData.groupby(
            'continent')['beer_servings'].mean())

        # 打印continent的wine_servings描述性统计值
        # describe 包括：计数、平均值、标准差、最小值、最大值等
        print(drinksData.groupby('continent').wine_servings.describe())

        # 打印出每个continent每种酒类的消耗平均值
        print(drinksData.groupby('continent').mean())

        # 打印出每个continent每种酒类的中位数
        print(drinksData.groupby('continent').median())

        # 打印出每个continent队spirit的平均值、最大值、最小值
        print(drinksData.groupby('continent')[
              'spirit_servings'].agg(['mean', 'max', 'min']))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice3()
    example.exercise()
