import pandas as pd
import numpy as np
from itertools import islice


def num_generator():
    prev = 10000
    while True:
        yield prev
        prev = prev + np.random.randint(1000, 5000)


ngen = num_generator()
num_list = list(islice(ngen, 0, 10))

# print(num_list)

country_list = ['China', 'Amarica', 'Russia', 'Japan', 'England',
                'Span', 'Italy', 'Mexico', 'Canada', 'German',
                'France', 'Australia', 'Newziland', 'Brazil', 'Poland']

dates = pd.date_range(start='20190101', end='20191231', freq='D')
values0 = np.random.randint(35000, high=75000, size=365)
values1 = np.random.randint(30000, high=60000, size=365)
values2 = np.random.randint(25000, high=55000, size=365)

df0 = pd.DataFrame({'name': 'num0', 'type': 'China',
                    'value': values0, 'date': dates})
df1 = pd.DataFrame({'name': 'num1', 'type': 'Amarica',
                    'value': values0, 'date': dates})
df2 = pd.DataFrame({'name': 'num2', 'type': 'Russia',
                    'value': values0, 'date': dates})
df3 = pd.DataFrame({'name': 'num3', 'type': 'Japan',
                    'value': values0, 'date': dates})
df4 = pd.DataFrame({'name': 'num4', 'type': 'England',
                    'value': values0, 'date': dates})
df5 = pd.DataFrame({'name': 'num5', 'type': 'Span',
                    'value': values1, 'date': dates})
df6 = pd.DataFrame({'name': 'num6', 'type': 'Italy',
                    'value': values1, 'date': dates})
df7 = pd.DataFrame({'name': 'num7', 'type': 'Mexico',
                    'value': values1, 'date': dates})
df8 = pd.DataFrame({'name': 'num8', 'type': 'German',
                    'value': values1, 'date': dates})
df9 = pd.DataFrame({'name': 'num9', 'type': 'France',
                    'value': values1, 'date': dates})
df10 = pd.DataFrame({'name': 'num10', 'type': 'Australia',
                     'value': values2, 'date': dates})
df11 = pd.DataFrame({'name': 'num11', 'type': 'Newziland',
                     'value': values2, 'date': dates})
df12 = pd.DataFrame({'name': 'num12', 'type': 'Brazil',
                     'value': values2, 'date': dates})
df13 = pd.DataFrame({'name': 'num13', 'type': 'Poland',
                     'value': values2, 'date': dates})
df14 = pd.DataFrame({'name': 'num14', 'type': 'Canada',
                     'value': values2, 'date': dates})

df = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7,
                df8, df9, df10, df11, df12, df13, df14], ignore_index=True)

df['value'] = np.random.randint(10000, high=100000, size=5475)
print(df.tail())
# df.to_csv('country_ranking_data_15.csv')
# print(df.info())
