"""
Functions for dealing with dataframe column names
"""

import pandas as pd

def inflate_cols(dataframe):
    """
    Given a DataFrame with collapsed multi-index columns this will
    return a pandas DataFrame index. that can be used like so:
        df.columns = inflate_columns(df)
    """
    header_1, header_2 = [], []
    for colname in dataframe.columns:
        name_split = colname.split()
        header_1.append(name_split[0])
        header_2.append(name_split[1])
    assert len(header_1) == len(header_2)
    tuples = zip(header_1, header_2)
    return pd.MultiIndex.from_tuples(tuples)


def collapse_cols(dataframe, sep="_"):
    """Given a dataframe, will collapse multi-indexed columns names"""
    return [sep.join(col).strip() for col in dataframe.columns.values]
