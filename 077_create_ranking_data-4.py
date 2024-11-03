import pandas as pd
import numpy as np
from itertools import islice


def num_generator():
    prev = np.random.randint(1000, 10000)
    while True:
        yield prev
        prev = prev + \
            np.random.randint(1000, 10000)


def china_generator():
    prev = np.random.randint(1000, 10000)
    while True:
        yield prev
        prev = prev + \
            np.random.randint(2000, 12000)


# ngen=num_generator()
# num_list = list(islice(ngen, 0, 10))
# s = pd.Series(list(islice(ngen, 0, 365)))

# print(num_list)

# country_list = ['China', 'Amarica', 'Russia', 'Japan', 'England',
#                 'Span', 'Italy', 'Mexico', 'Canada', 'German',
#                 'France', 'Australia', 'Newziland', 'Brazil', 'Poland']

dates = pd.date_range(start='20190101', end='20191231', freq='D')

df0 = pd.DataFrame({'name': '人口', 'type': 'China',
                    'value': pd.Series(list(islice(china_generator(), 0, 365))), 'date': dates})
df1 = pd.DataFrame({'name': 'A', 'type': 'Amarica',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df2 = pd.DataFrame({'name': 'B', 'type': 'Russia',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df3 = pd.DataFrame({'name': 'C', 'type': 'Japan',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df4 = pd.DataFrame({'name': 'D', 'type': 'Span',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df5 = pd.DataFrame({'name': 'E', 'type': 'Italy',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df6 = pd.DataFrame({'name': 'F', 'type': 'Mexico',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df7 = pd.DataFrame({'name': 'G', 'type': 'Canada',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df8 = pd.DataFrame({'name': 'H', 'type': 'German',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df9 = pd.DataFrame({'name': 'I', 'type': 'France',
                    'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df10 = pd.DataFrame({'name': 'J', 'type': 'Australia',
                     'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df11 = pd.DataFrame({'name': 'K', 'type': 'Newziland',
                     'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df12 = pd.DataFrame({'name': 'L', 'type': 'Brazil',
                     'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df13 = pd.DataFrame({'name': 'M', 'type': 'England',
                     'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})
df14 = pd.DataFrame({'name': 'N', 'type': 'Poland',
                     'value': pd.Series(list(islice(num_generator(), 0, 365))), 'date': dates})

df = pd.concat(
    [df0, df1, df2, df3, df4, df5, df6, df7,
        df8, df9, df10, df11, df12, df13, df14],
    ignore_index=True)

# print(df.tail())
# print(df.info())
# df.to_csv('country_ranking_data_15.csv')
df.to_csv('~/GitHub/Historical-ranking-data-visualization-based-on-d3.js/src/country_ranking_data_15.csv')
