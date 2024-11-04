import os
from numpy import NaN, float64, int64
import pandas as pd
import datetime

"""把从东方财富保存的沪深300股票行情数据进行清理，另存csv。"""


def getTodayFile(orgDir, orgFileName):
    orgFilePath = os.path.join(orgDir, orgFileName)
    df = pd.read_csv(orgFilePath, encoding='ANSI')
    return df


def save_csv_file(df, saveDir, saveFileName):
    savePath = os.path.join(saveDir, saveFileName)
    df.to_csv(savePath)


def print2see(df):
    print(df.head())
    # print(df.tail())
    print(df.columns)
    # print(df.describe)
    # print(df.info())
    # print(df.dtypes)
    # print(df.shape)
    # print(df)
    # print(df.iloc[:6, [-1]])


def str2value(xl):    #——，亿，万，变成0或整数
    if xl == '—':
        return 0
    elif str(xl).find('万亿') != -1:
        return int64(float(str(xl).strip('万亿'))*1e12)
    elif str(xl).find('亿') != -1:
        return int64(float(str(xl).strip('亿'))*1e8)
    elif str(xl).find('万') != -1:
        return int64(float(str(xl).strip('万'))*1e4)
    else:
        return int(xl)


def cleanFile(df):
    outMarkeCsv = r'E:\stockData\eastMoney\delete_symbol.csv'
    outMarketDf = pd.read_csv(outMarkeCsv)
    outMarketList = outMarketDf['code'].to_list()    #退市股票列表

    newColList = df.columns.str.split('\\t').to_list()[0]
    contentSeries = df.iloc[:, 0]
    dfnew= contentSeries.str.split('\\t', expand=True)     #Series to DataFrame
    dfnew.columns = newColList    #add columns

    dn = dfnew.drop(columns=['序', ''], axis=1)
    dn['名称'] = dn['名称'].str.strip()
    dn['所属行业'] = dn['所属行业'].str.strip()
    dn['代码'] = dn['代码'].str.replace('= ', '')
    dn['代码'] = dn['代码'].str.replace('"', '')
    dn['代码'] = dn['代码'].apply(pd.to_numeric, downcast='integer')
    dn = dn[~dn['代码'].isin([i for i in outMarketList])]    #删除退市的股票

    cols1 = [2, 3, 4, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 25, 28, 33, 34, 35, 36]
    dn.iloc[:, [x for x in cols1]] = dn.iloc[:, [x for x in cols1]].apply(pd.to_numeric, errors='coerce', downcast='float')

    # 处理有亿万等字眼的列，去除空格
    collist = [x for x in dn.columns]
    cols2 = [5, 6, 11, 21, 23, 24, 26, 27, 29, 30, 31, 32]  #有亿万字眼的列
    cols3 = []
    for colIndex in cols2:
        cols3.append(collist[colIndex])
        for colName in cols3:
            dn[colName] = dn[colName].str.strip()

    for colName1 in cols3:
        dn[colName1] = dn[colName1].apply(str2value)
    return dn


if __name__ == "__main__":
    today = datetime.date.today()
    # today = '2021-08-30'
    orgFileName = 'stock_hs_{}.csv'.format(today)
    orgDir = r'E:\stockData\eastMoney'
    saveDir = orgDir + '\cleaned'
    # saveFileName = orgFileName[:-4] + '_clean.csv'
    saveFileName = '{}'.format(today) + '_' + orgFileName[:-15] + '_clean.csv'

    df = getTodayFile(orgDir, orgFileName)
    dn = cleanFile(df)
    # print2see(dn)
    print(dn.金额.sum(axis=0, skipna=True))
    save_csv_file(dn, saveDir, saveFileName)