'''
@Description: code
@Author: MiCi
@Date: 2020-03-13 17:17:47
@LastEditTime: 2020-03-14 08:47:08
@LastEditors: MiCi
'''

import pandas as pd
# import numpy as np


class Basic4(object):

    def __init__(self):
        return

    def basic_use(self):
        df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3'],
                            'C': ['C0', 'C1', 'C2', 'C3'],
                            'D': ['D0', 'D1', 'D2', 'D3']},
                           index=[0, 1, 2, 3])

        df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                            'B': ['B4', 'B5', 'B6', 'B7'],
                            'C': ['C4', 'C5', 'C6', 'C7'],
                            'D': ['D4', 'D5', 'D6', 'D7']},
                           index=[4, 5, 6, 7])
        # append末尾追加数据
        print(df1.append(df2))

        # concat列后添加
        print(pd.concat([df1, df2], axis=1))

        # join做内连接，on=col为连接列
        df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                            'B': ['B0', 'B1', 'B2', 'B3'],
                            'key': ['K0', 'K1', 'K0', 'K1']})

        df2 = pd.DataFrame({'C': ['C0', 'C1'],
                            'D': ['D0', 'D1']},
                           index=['K0', 'K1'])

        print(df1.join(df2, on='key'))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Basic4()
    example.basic_use()
