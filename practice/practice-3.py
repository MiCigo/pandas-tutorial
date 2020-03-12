'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 21:11:37
@LastEditTime: 2020-03-12 21:47:58
@LastEditors: MiCi
'''

import pandas as pd


class Practice3(object):

    def __init__(self):
        return

    def exercise(self):
        path = './data/drinks.csv'
        dinksData = pd.read_csv(path)
        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice3()
    example.exercise()
