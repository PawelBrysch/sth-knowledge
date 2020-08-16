import pandas as pd
import os


def get_some_df():
    return pd.read_pickle(os.path.abspath("sth.pickle"))


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




