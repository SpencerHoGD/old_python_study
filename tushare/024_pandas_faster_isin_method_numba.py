import pandas as pd
import numpy as np
# import numba
import timeit


def create_kwh_df_pkl(rows):
    datetime1 = pd.date_range(start='1/1/1970', periods=rows, freq='H')
    kwh = np.random.random_sample(rows)

    df = pd.DataFrame({'date_time': datetime1, 'energy_kwh': kwh})
    # df.to_csv('energy_kwh.csv')
    df.to_pickle('energy_kwh.pkl')


# 编写求得相应结果的函数
def get_cost(kwh, hour):
    if 0 <= hour < 7:
        rate = 0.6
    elif 7 <= hour < 17:
        rate = 0.68
    elif 17 <= hour < 24:
        rate = 0.75
    else:
        raise ValueError(f'Invalid hour: {hour}')
    return rate * kwh


# 方法一：简单循环
def loop(df):
    cost_list = []
    for i in range(len(df)):
        energy_used = df.iloc[i]['energy_kwh']
        hour = df.iloc[i]['date_time'].hour
        energy_cost = get_cost(energy_used, hour)
        cost_list.append(energy_cost)
    df['cost'] = cost_list


# 方法二：apply方法
def apply_method(df):
    df['cost'] = df.apply(
        lambda row: get_cost(
            kwh=row['energy_kwh'],
            hour=row['date_time'].hour),
        axis=1)
    # print(df.tail(20))
    # print(df['cost'].agg(sum))


# 方法三：采用isin筛选出各时段，分段处理
def isin_method(df):
    df.set_index('date_time', inplace=True)

    peak_hours = df.index.hour.isin(range(17, 24))
    simple_hours = df.index.hour.isin(range(7, 17))
    off_peak_hours = df.index.hour.isin(range(0, 7))

    # df.loc[peak_hours, 'rate'] = 0.75
    # df.loc[simple_hours, 'rate'] = 0.68
    # df.loc[off_peak_hours, 'rate'] = 0.6

    df.loc[peak_hours, 'cost'] = df.loc[peak_hours, 'energy_kwh'] * 0.75
    df.loc[simple_hours, 'cost'] = df.loc[simple_hours, 'energy_kwh'] * 0.68
    df.loc[off_peak_hours, 'cost'] = df.loc[off_peak_hours, 'energy_kwh'] * 0.6

    print(df.tail())
    print(df['cost'].agg(sum))


if __name__ == '__main__':
    num1 = 2*10**6
    create_kwh_df_pkl(num1)
    # df = pd.read_csv('energy_kwh.csv')
    df = pd.read_pickle('energy_kwh.pkl')
    # print(df.tail())

    # t4 = timeit.timeit('create_kwh_df_pkl(num1)', number=1, globals=globals())
    # print(t4)
    # t5 = timeit.timeit(lambda: pd.read_pickle('energy_kwh.pkl'), number=1)
    # print(t5)
    # t1 = timeit.timeit('loop(df)', number=1, globals=globals())
    # print(t1)
    # t2 = timeit.timeit('apply_method(df)', number=1, globals=globals())
    # print(t2)

    t3 = timeit.timeit('isin_method(df)', number=1, globals=globals())
    print(t3)

    # v21 = (1/t2)/(1/t1)
    # print(v21)
    # v31 = (1/t3)/(1/t1)
    # print(v31)

    # 124.35倍
    # v32 = (1/t3)/(1/t2)
    # print(v32)
