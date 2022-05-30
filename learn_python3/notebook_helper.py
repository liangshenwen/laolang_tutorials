import pandas as pd
import numpy as np


def highlight(series:pd.Series, color:str = 'yellow'):
    return 'background-color: %s' % color


def highlight_columns(df:pd.DataFrame, cols:list, color:str = 'yellow'):
    return df.style.applymap(highlight, color=color, subset=cols)


def ahead_df_columns(df:pd.DataFrame, cols:list):
    columns = list(df.columns)
    cols.reverse()
    for col in cols:
        if col in columns:
            columns.remove(col)
            columns.insert(0, col)

    return df.loc[:, columns]