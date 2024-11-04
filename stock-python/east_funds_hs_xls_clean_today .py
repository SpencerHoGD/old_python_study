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
    newColList = df.columns.str.split('\\t').to_list()[0]
    contentSeries = df.iloc[:, 0]
    dfnew= contentSeries.str.split('\\t', expand=True)     #Series to DataFrame
    dfnew.columns = newColList    #add columns

    dn = dfnew.drop(columns=['序', ''], axis=1)
    dn['名称'] = dn['名称'].str.strip()
    dn = dn[~dn['金额'].isin([' —'])]    #删除金额为0或——
    dn = dn[~dn['开盘'].isin([' —'])]    #删除金额为0或——
    dn['代码'] = dn['代码'].str.replace('= ', '')
    dn['代码'] = dn['代码'].str.replace('"', '')
    dn['代码'] = dn['代码'].apply(pd.to_numeric, downcast='integer')
    dn.set_index('代码')

    columnsList = dn.columns.to_list()
    colsStrIndex = [5, 6, 10, 19, 20, 22, 23]    #有亿万字眼的列
    colsValueIndex = set(list(range(len(columnsList)))[2:]).difference(set(colsStrIndex))
    # print(colsValueIndex)
    # print(colsHavevalue)
    dn.iloc[:, [x for x in colsValueIndex]] = dn.iloc[:, [x for x in colsValueIndex]].apply(pd.to_numeric, errors='coerce', downcast='float')

    # 处理有亿万等字眼的列，去除空格
    collist = [x for x in dn.columns]
    cols3 = []
    for colIndex in colsStrIndex:
        cols3.append(collist[colIndex])
        for colName in cols3:
            dn[colName] = dn[colName].str.strip()

    for colName1 in cols3:
        dn[colName1] = dn[colName1].apply(str2value)

    return dn


def print2see(df):
    print(df.head())
    # print(df.tail())
    # print(df.columns)
    print(df.describe)
    # print(df.info())
    # print(df.dtypes)
    # print(df.shape)
    # print(df)
    print(df.iloc[:6, [0]])


if __name__ == "__main__":
    today = datetime.date.today()
    # today = '2021-08-30'
    shFilename = 'funds_sh_{}.csv'.format(today)
    szFileName = 'funds_sz_{}.csv'.format(today)
    fileNameList = [shFilename, szFileName]
    orgDir = r'E:\stockData\eastMoney'
    saveDir = orgDir + '\cleaned'

    for orgFileName in fileNameList:
        df = getTodayFile(orgDir, orgFileName)
        dn = cleanFile(df)
        # print2see(dn)
        print(dn.金额.sum(axis=0, skipna=True))
        # saveFileName = orgFileName[:-4] + '_clean.csv'
        saveFileName = '{}'.format(today) + '_' + orgFileName[:-15] + '_clean.csv'
        save_csv_file(dn, saveDir, saveFileName)