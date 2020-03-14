'''
@Description: code
@Author: MiCi
@Date: 2020-03-14 15:24:08
@LastEditTime: 2020-03-14 20:52:10
@LastEditors: MiCi
'''

import pandas as pd
import numpy as np


class Practice5(object):

    def __init__(self):
        return

    def exercise(self):
        raw_data_1 = {
            'subject_id': ['1', '2', '3', '4', '5'],
            'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
            'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

        raw_data_2 = {
            'subject_id': ['4', '5', '6', '7', '8'],
            'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
            'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

        raw_data_3 = {
            'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
            'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

        data1 = pd.DataFrame(raw_data_1, columns=[
                             'subject_id', 'first_name', 'last_name'])
        data2 = pd.DataFrame(raw_data_2, columns=[
                             'subject_id', 'first_name', 'last_name'])
        data3 = pd.DataFrame(raw_data_3, columns=['subject_id', 'test_id'])

        # 列合并data1 + data2
        nameData = pd.concat([data1, data2], axis=1)
        print(nameData)

        # 行合并data1 + data2
        nameData = pd.concat([data1, data2])
        print(nameData)

        # 用subject_id连接合并nameData + data3
        print(pd.merge(nameData, data3, on='subject_id'))

        # 用subject_id连接data1 + data2
        print(pd.merge(data1, data2, on='subject_id'))

        # 用subject_id做全连接data1 + data2
        print(pd.merge(data1, data2, on='subject_id', how='outer'))

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice5()
    example.exercise()
