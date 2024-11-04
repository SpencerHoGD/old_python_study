from zipfile import ZipFile
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import json


# filepath = r'F:\FirefoxDownloads\ExStudy.zip'
# filepath1 = '/Users/hexiaoming/Downloads/ExStudy.zip'
# zf = ZipFile(filepath1, 'r')
# zf.extractall()
# zf.close()

date1 = '20190927'
f1 = poloniex_filename = 'poloniex-trades-{}.json'.format(date1)
f2 = binance_filename = 'binance-trades-{}.json'.format(date1)
f3 = coinbase_filename = 'coinbase-trades-{}.json'.format(date1)
f4 = mxc_filename = 'mxc-trades-{}.json'.format(date1)

poloniex_trades = json.loads(open(f1).read())
binance_trades = json.loads(open(f2).read())
coinbase_trades = json.loads(open(f3).read())
mxc_trades = json.loads(open(f4).read())

poloniex_df = pd.DataFrame({'price': [float(i['p']) for i in poloniex_trades],
                            'size': [float(i['q']) for i in poloniex_trades],
                            'time': [i['t'] for i in poloniex_trades]
                            })
binance_df = pd.DataFrame({'price': [float(i['p']) for i in binance_trades],
                           'size': [float(i['q']) for i in binance_trades],
                           'time': [i['t'] for i in binance_trades]
                           })
coinbase_df = pd.DataFrame({'price': [float(i['p']) for i in coinbase_trades],
                            'size': [float(i['q']) for i in coinbase_trades],
                            'time': [i['t'] for i in coinbase_trades]
                            })
mxc_df = pd.DataFrame({'price': [float(i['p']) for i in mxc_trades],
                       'size': [float(i['q']) for i in mxc_trades],
                       'time': [i['t'] for i in mxc_trades]
                       })

# print('{} len:'.format(f1) + str(len(poloniex_trades)))
# print('{} len:'.format(f2) + str(len(binance_trades)))
# print('{} len:'.format(f3) + str(len(coinbase_trades)))
# print('{} len:'.format(f4) + str(len(mxc_trades)))

ex_list = ['poloniex', 'binance', 'coinbase', 'mxc']
sum_of_size = [
    sum(poloniex_df['size']),
    sum(binance_df['size']),
    sum(coinbase_df['size']),
    sum(mxc_df['size'])
]
monthly_total_visit = [25*10**5, 205*10**5, 227*10**5, 38*10**4]
size_per_visit = [i/(j/30) for i, j in zip(sum_of_size, monthly_total_visit)]
# sns.barplot(x=ex_list, y=sum_of_size)
# sns.barplot(x=ex_list, y=monthly_total_visit)
# sns.barplot(x=ex_list, y=size_per_visit)


def plot_trade_size(df, cap, nbins):
    # select capped trades
    size = df.loc[df['size'] <= cap]['size']
    # categary
    bins = pd.Series(np.linspace(0, cap, nbins + 1))
    # cut by categary
    out = pd.cut(size, bins)
    # normalize to pct
    out_norm = out.value_counts(sort=False, normalize=True).mul(100)
    # plot
    x = out_norm.index
    y = out_norm
    sns.set(style='darkgrid')
    plt.figure(figsize=(24, 6))
    plt.xticks(rotation=90)
    ax = sns.barplot(x=x, y=y)

    plt.ylabel("pct")
    plt.show()


# plot_trade_size(poloniex_df, 4, 100)
# plot_trade_size(binance_df, 4, 100)
# plot_trade_size(coinbase_df, 4, 100)
# plot_trade_size(mxc_df, 4, 100)
