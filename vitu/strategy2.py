from vitu import ai
ai.create_account(name='myaccount', exchange='binance', account_type='digital.spot', position_base=[{'asset': 'USDT', 'qty': 10000}])

def initialize(context):
        context.security = 'BTC/USDT.binance'
        context.myaccount = context.get_account('myaccount')

def handle_data(context):
        current_price = context.get_price(context.security)
        context.myaccount.buy(context.security, current_price, 0.1)
        print("当前触发时间: %s" % context.current_datetime())

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