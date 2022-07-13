import streamlit as st 
import pandas as pd
from helper_clean import data_clean 


portfolio_data = st.file_uploader("2022-06-27-AccountStatement.csv")


    
if portfolio_data is not None: 
    df = pd.read_csv(portfolio_data)
    
    tickers, quantity = data_clean(df)

    st.write(tickers)
    st.write(quantity)
    
    
    
    

