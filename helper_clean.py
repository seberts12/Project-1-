import pandas as pd 

def data_clean(my_df):
    tickers = list(my_df.iloc[54:58, 0])
    quantity = list(my_df.loc[54:57, "Unnamed: 2"])
    return tickers, quantity

