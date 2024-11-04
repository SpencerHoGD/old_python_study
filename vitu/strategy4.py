from vitu import ai 
import numpy as np


ai.create_account(name='myaccount', exchange='binance', 
                  account_type='digital.spot', 
                  position_base=[{'asset':'USDT','qty':10000}])


def initialize(context):
  context.MA_length = 10
  context.myaccount = context.get_account('myaccount')
  context.securities = ['BTC/USDT.binance', 'ETH/USDT.binance']


def handle_data(context):
    for symbol in context.securities:
        close_price = context.history(symbol, 'close', 
                                      bars=context.MA_length, 
                                      rtype='ndarray')
        MA10 = np.mean(close_price)                              
        current_price = context.get_price(symbol)
        if (current_price > MA10):
            context.myaccount.buy_pct(symbol, current_price, 0.1)
        elif (current_price < MA10):
            context.myaccount.sell_pct(symbol, current_price, 1)


universe = ai.create_universe(['BTC/USDT.binance', 'ETH/USDT.binance'])

my_strategy = ai.create_strategy(
    initialize,
    handle_data,
    universe=universe,
    benchmark='csi5',
    freq='d',
    refresh_rate = 1    
)

ai.backtest(
    strategy=my_strategy,
    start='2018-12-10',
    end='2019-08-10',
    commission={'taker':0.0002, 'maker':0.0002}
)