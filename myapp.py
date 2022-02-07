import yfinance as yf
import streamlit as st
import pandas as pd


@st.cache

def page():
     st.set_page_config(layout="wide")




st.write(
    """
    # Company Stocks app

    shown are the closing prices and volume of companies


    """
    
)

company_name = st.text_input("Please Enter the Comapny Code")

tickerSymbol = company_name

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start = '2011-5-31', end = '2021-12-31')




col1, col2 = st.columns(2)

with col1:
    st.write(
    """
    # Closing Price
    """
    
     )
    st.line_chart(tickerDf.Close)

with col2:
    st.write(
    """
    # Volume Price
    """
    
    )
    st.line_chart(tickerDf.Volume)


col3, col4 = st.columns(2)

with col3:
    st.write(
    """
    # High index 
    """
    
     )
    st.line_chart(tickerDf.High)

with col4:
    st.write(
    """
    # Low Index 
    """
    
    )
    st.line_chart(tickerDf.Low)







genre = st.radio(
     "Do you want Yearly or Quaterly Financial",
     ('Yearly', 'Quaterly'))

if genre == 'Yearly':
     st.write('The Yearly Financials')
     st.dataframe(tickerData.financials)
else:
     st.write("The Quaterly Financials")
     st.dataframe(tickerData.quarterly_financials)




earn = st.radio(
     "Do you want Yearly or Quaterly Earning",
     ('Yearly', 'Quaterly'))

if earn == 'Yr':
     st.write('The Yearly Financials')
     st.dataframe(tickerData.earnings)
else:
     st.write("The Quaterly Financials")
     st.dataframe(tickerData.quarterly_earnings)

st.write("""
# The major stock holders in the company 

"""
)

st.dataframe(tickerData.major_holders)

news = tickerData.news

st.header("Finance News")

for i in news:
    st.write(i['title'])
    st.write("Author : ", i['publisher'])
    link_news = i['link']
    st.write("link to the article [Link](%s)",link_news)
    


