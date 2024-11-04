import pandas as pd
import timeit


def manipulate_files():
    df = pd.read_csv('daily_2018.csv')
    df.to_pickle('daily_2018.pkl')
    df.to_hdf('daily_2018.hdf', 'df')


def test_timeit():
    num = 5
    csv_timer = timeit.timeit(
        lambda: pd.read_csv('daily_2018.csv'), number=num)
    pkl_timer = timeit.timeit(
        lambda: pd.read_pickle('daily_2018.pkl'), number=num)
    # hdf_timer = timeit.timeit(
    #     lambda: pd.read_hdf('daily_2018.hdf', 'df'), number=num)

    num2 = 50
    print('-' * num2)
    print(csv_timer)
    print(pkl_timer)
    # print(hdf_timer)
    print('-' * num2)

    pvc = (1/pkl_timer)/(1/csv_timer)
    # hvc = (1/hdf_timer)/(1/csv_timer)
    # pvh = (1/pkl_timer)/(1/hdf_timer)
    print(pvc)
    # print(hvc)
    # print(pvh)
    print('-' * num2)


def read_pkl_file():
    df = pd.read_pickle('daily_2018.pkl')
    print(df.tail())


if __name__ == '__main__':
    # manipulate_files()
    # test_timeit()
    read_pkl_file()
