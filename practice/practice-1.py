'''
@Description: code
@Author: MiCi
@Date: 2020-03-12 08:55:59
@LastEditTime: 2020-03-12 21:46:09
@LastEditors: MiCi
'''

import pandas as pd


class Practice1(object):

    def __init__(self):
        return

    def exercise(self):
        path = "./data/chipotle.tsv"
        # 读取数据集
        chipo = pd.read_csv(path, sep='\t')

        # 读取前n行
        print(chipo.head(3))

        # shape[1]返回列数，shape[0]返回行数，读取columns数量
        print('Columns:', chipo.shape[1])

        # 读取数据集列名
        print(chipo.columns)

        # 读取数据集索引
        print(chipo.index)

        # 选出下单量最大的商品item
        # groupby商品名 + agg聚合函数{'行/列','函数名'}
        itemCount = chipo[['item_name', 'quantity']].groupby(
            ['item_name'], as_index=False).agg({'quantity': sum})
        # sort_values：by用来指定排序元素，ascending默认为True即为升序，false反之
        # inplace 为一个特殊的算法：https://en.wikipedia.org/wiki/In-place_algorithm
        # kind参数使用什么算法排序，quicksort快排、mergesort归并排序等
        # na_position 针对DataFrame中的空缺值防止位置，默认值last放在排序最后
        itemCount.sort_values(by=['quantity'], ascending=False, inplace=True)
        print(itemCount.head(3))

        # nuinque查看序列不同值的数量
        print('Unique Item:', chipo['item_name'].nunique())

        # value_counts查看choice_desription中下单次数最大的商品
        print(chipo['choice_description'].value_counts().head(3))

        # sum求和，一共下单多少件商品
        print('Total Orders:', chipo['quantity'].sum())

        # 利用apply自定义处理方法，将item_price转换为浮点数
        def priceTrans(x): return float(x[1:-1])
        chipo['item_price'] = chipo['item_price'].apply(priceTrans)

        # 统计总收入
        chipo['sub_total'] = round(chipo['item_price'] * chipo['quantity'], 2)
        print('Total Revenue:', chipo['sub_total'].sum())

        # 统计总订单数
        print('Total Order num:', chipo['order_id'].nunique())

        # 统计平均订单价，利用mean函数求轴向数据平均值
        avgOrderPrice = chipo[['order_id', 'sub_total']].groupby(
            by=['order_id']).agg({'sub_total': 'sum'})['sub_total'].mean()
        print('Avg Order Price:', avgOrderPrice)

        return


if __name__ == '__main__':
    print('Start Learn Pandas')
    print('============================\n')
    example = Practice1()
    example.exercise()
