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
"""
1. jak nalezy czytac linijke z agg?->                         argument bedacy indeksem listy jest przekazywany do lambdy
2. skoro jest to agregacja, to->                                                       funkcje raczej nie beda customowe
"""
# import pandas as pd
# df = pd.DataFrame.from_dict({
#     'IS_RICH':      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#     'STUDY_ABROAD': [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
# })
#
# summary = df.groupby('IS_RICH')['STUDY_ABROAD'].agg(lambda x: x.mean())
# print(summary)


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


"""******************************************
DF.apply()
******************************************"""
"""axis=1 -> po wierszach -> powstaje nowa kolumna"""
# import pandas as pd
# from typing import Any
#
# df = pd.DataFrame.from_dict({
#     'width': [1, 2, 3],
#     'length': [6, 5, 4]
# })
#
# def area(single_row_df: pd.DataFrame) -> Any:
#     return single_row_df['width'] * single_row_df['length']
#
# df = df.assign(
#     area=df.apply(area, axis=1)
# )
#
# print(df)

"""axis=0 -> po kolumnach -> zachodzi pewnego rodzaju agregacja"""
"""
Tutaj raczej nie przychodzi mi nic innego jak zagregowanie Series'a do jakiejs wartosci.
Z tego powodu czesciej bedzie sie uzywalo gotowych funkcji zamiast customowych.
"""
# import pandas as pd
#
# df = pd.DataFrame.from_dict({
#     'x': [1, 2, 3],
#     'y': [6, 5, 4]
# })
#
# geometric_center = df.apply(pd.Series.mean, axis=0)
#
# print(geometric_center)