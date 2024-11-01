import pandas as pd
from datetime import datetime


def gen_Q1():
    filename1 = '2020_Q1th.md'
    dates = pd.date_range(start='20200101', end='20200331', freq='D')
    with open(filename1, 'w') as f:
        for date in dates:
            day = date.strftime('%d')
            month = date.strftime('%m')
            contents_list = '[' + day + ']' + \
                            '(' + '#' +\
                            date.strftime('%Y/%m/%d %a') + \
                            '. Day' + date.strftime('%j') + \
                            ' Week' + date.strftime('%W') + ') '
            if day.startswith("01"):
                f.write('\n' * 2 + month + '\n' + contents_list)
            else:
                f.write(contents_list)

        f.write('\n' * 5)

        for date in dates:
            f.write('## ' +
                    date.strftime('%Y/%m/%d %a') +
                    '. Day' + date.strftime('%j') +
                    ' Week' + date.strftime('%W') + '\n')




if __name__ == '__main__':
    gen_Q1()
