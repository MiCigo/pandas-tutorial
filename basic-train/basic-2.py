'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 15:04:12
@LastEditTime: 2020-03-12 15:06:40
@LastEditors: MiCi
'''

import pandas as pd


class Basic2(object):

    def __init__(self):
        return

    def basic_use(self):
        path = './data/Euro2012_stats.csv'

        euroData = pd.read_csv(path)
        print(euroData)

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic2()
    example.basic_use()
