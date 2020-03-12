'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 21:11:37
@LastEditTime: 2020-03-12 21:43:21
@LastEditors: MiCi
'''

import pandas as pd


class Basic3(object):

   def __init__(self):
        return

    def basic_use(self):
        path = './data/drinks.csv'
        dinksData = pd.read_csv(path)
        return

if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic3()
    example.basic_use()
