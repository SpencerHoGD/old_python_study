from vitu import ai
ai.create_account(name='myaccount', exchange='binance', account_type='digital.spot', position_base=[{'asset': 'USDT', 'qty': 10000}])

def initialize(context):
        context.security = 'BTC/USDT.binance'
        context.myaccount = context.get_account('myaccount')

def handle_data(context):
        current_price = context.get_price(context.security)
        context.myaccount.buy(context.security, current_price, 0.1)
        print("当前触发时间: %s" % context.current_datetime())
        #获取持仓
        current_position = context.myaccount.get_position('BTC')
        cost = current_position['avg_cost_usdt']
        print(current_position)
        #计算收益率
        ret = current_price/cost-1
        #打印日志
        print('成本价：%s' % cost)
        print('现价：%s' % current_price)
        print('收益率：%s' % ret)
        # 如果收益率小于-0.01，即亏损达到1%则卖出标的，幅度可以自己调
        if ret < -0.01:
            context.myaccount.sell_pct(context.security, current_price, 1)
            print('触发止损')

universe = ai.create_universe(['BTC/USDT.binance'])

my_strategy = ai.create_strategy(
        initialize,
        handle_data,
        universe=universe,
        benchmark='csi5',
        freq='d',
        refresh_rate=1
)

ai.backtest(strategy=my_strategy,
        start='2018-12-10',
        end='2019-08-10',
        commission={'taker': 0.0002, 'maker': 0.0002}
)