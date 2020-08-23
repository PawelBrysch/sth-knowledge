import pandas as pd
import os


def get_some_df():
    return pd.read_pickle(os.path.abspath("sth.pickle"))

# TODO cale do powtorki

"""******************************************
AGGREGATION
******************************************"""
"""
+-----------+-----------+--------------+
| METHOD    | RETURNS   | 1 CELL FROM  |
+-----------+-----------+--------------+
| transform | Series    | 1 cell       |
+-----------+-----------+--------------+
| agg       | Series    | 1 group      | !!! wiele BUILD-INow !!! .min(), .size(), etc.
+-----------+-----------+--------------+
| filter    | Dataframe | n/a          |
+-----------+-----------+--------------+
"""
"""transform()"""
# df = get_some_df()
# sth1 = 'artist'
# sth2 = "medium"
#
# def some_func(series: pd.Series) -> pd.Series:
#     # do sth
#     return series
#
# iterator_of_dfs_grouped_by_sth1 = df.groupby(sth1)
# iterator_of_series_of_sth2_grouped_by_sth1 = iterator_of_dfs_grouped_by_sth1[sth2]
# transformed_series_of_sth2 = iterator_of_series_of_sth2_grouped_by_sth1.transform(some_func)

"""agg()"""
import random
from typing import Any

df = get_some_df()
sth1 = 'artist'
sth2 = 'acquisitionYear'

def some_func(series: pd.Series) -> Any:
    # do sth
    return random.randint(0, 10)

iterator_of_dfs_grouped_by_sth1 = df.groupby(sth1)
iterator_of_series_of_sth2_grouped_by_sth1 = iterator_of_dfs_grouped_by_sth1[sth2]
result = iterator_of_series_of_sth2_grouped_by_sth1.agg(some_func)


"""filter()"""
# df = get_some_df()
# sth1 = 'artist'
#
# def some_func(series: pd.DataFrame) -> bool:
#     # do sth
#     return True
#
# iterator_of_dfs_grouped_by_sth1 = df.groupby(sth1)
# filtered_df = iterator_of_dfs_grouped_by_sth1.filter(some_func)


"""******************************************
FILTER without (!) aggregation
******************************************"""
# import pandas as pd
#
# df = pd.DataFrame.from_dict({
#     'X': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#     'Y': [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80]
# })
# # df = df[(abs(df.Y) <= 50)]
# df[(abs(df.Y) <= 50)]
# print(df)



