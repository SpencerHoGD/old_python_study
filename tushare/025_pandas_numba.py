import pandas as pd
import numpy as np
import numba
import timeit


def create_kwh_df_pkl():
    rows = 2*10**6
    datetime1 = pd.date_range(start='1/1/1970', periods=rows, freq='H')
    # print(datetime1)
    kwh = np.random.random_sample(rows)
    # print(kwh)

    df = pd.DataFrame({'date_time': datetime1, 'energy_kwh': kwh})
    # print(df.tail())
    # df.to_csv('energy_kwh.csv')
    df.to_pickle('energy_kwh.pkl')


def read_pkl_file():
    df = pd.read_pickle('energy_kwh.pkl')
    print(df.tail())
    return df


@numba.vectorize
def f_with_numba(x):
    return x * 2


def f_without_numba(x):
    return x * 2


def apply_way(df):
    # 方法一：apply逐行操作
    df["double_energy"] = df.energy_kwh.apply(f_without_numba)
    print(df.tail())


def vectorize_way(df):
    # 方法二：向量化运行
    df["double_energy"] = df.energy_kwh*2
    print(df.tail())


def numba_way(df):
    # 方法三：运用numba加速
    # 需要以numpy数组的形式传入
    # 否则会报错
    df["double_energy"] = f_with_numba(df.energy_kwh.to_numpy())
    print(df.tail())


def main():
    print(timeit.timeit('apply_way(df)', number=1, globals=globals()))  # 0.615 S
    print(timeit.timeit('vectorize_way(df)',
                        number=1, globals=globals()))  # 0.029 S
    print(timeit.timeit('numba_way(df)', number=1, globals=globals()))  # 0.199 S


if __name__ == '__main__':
    # create_kwh_df_pkl()
    df = read_pkl_file()
    main()
