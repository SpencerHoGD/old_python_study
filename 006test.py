from datetime import datetime
import pandas as pd


filename1 = '2020_Q1th.md'
filename2 = '2020_Q2nd.md'
filename3 = '2020_Q3rd.md'
filename4 = '2020_Q4th.md'
dates = pd.date_range(start='20200101', end='20200331', freq='D')
now = datetime.now()
# print('## ' + now.strftime('%a %b %d %H:%m'))
print('[' + now.strftime('%d') + ']' +
      '(' +
      now.strftime('%Y/%m/%d %a') +
      ' day=' + now.strftime('%j') +
      ' week=' + now.strftime('%W') +
      ')')
# print('## ' + now.strftime('%Y/%m/%d %a') +
#       ' day=' + now.strftime('%j') +
#       ' week=' + now.strftime('%W'))
# with open(filename1, 'w') as f:
#     for date in dates:
#         f.write('## ' + date.strftime('%Y/%m/%d %a') +
#                 '. day' + date.strftime('%j') +
#                 ' week' + date.strftime('%W') +
#                 '\n')
