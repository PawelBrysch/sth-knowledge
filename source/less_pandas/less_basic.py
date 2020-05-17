import pandas as pd
import os

def get_some_df():
    return pd.read_pickle(os.path.abspath("sth.pickle"))

"""############################
READING
############################"""
"""set index"""
# import pandas as pd
# import os
#
# some_column_name = ...
# tut_columns = pd.read_csv(os.path.abspath("artwork_data.csv"), index_col=some_column_name)


"""###########################
`LOC`
###########################"""
"""
a `iloc`? ->                                                                                          jak zwykle slicing
"""
# df = get_some_df()
#
# some_row_indexer = df["artist"]=='Blake, Robert'        # it is a Series indeed
# some_column_indexer = ["title", "year"]
#
# df_reduced_in_two_dimensions = df.loc[
#     some_row_indexer,
#     some_column_indexer
# ]


"""###########################
BIG OBJECTS ADDING
###########################"""
"""create new column"""
# df = df.assign(some_colume_name=some_series)

"""adding groups"""
# list_of_groups = ... #List[Dataframe]
# new_df = pd.concat(list_of_groups)


"""###########################
TYPE CONVERSION
###########################"""
"""to float"""
# df = get_some_df()
# some_column_name = 'width'
#
# df.loc[:, some_column_name] = pd.to_numeric(
#     df[some_column_name],
#     errors="coerce"         # wymusza zmiane na NaN, gdy sie nie da
# )


