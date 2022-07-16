import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write("""
# Simple Stock Price App

""")

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date > end_date:
    st.error('Error: End date must fall after start date.')

selectOptions = st.selectbox(  'Select the Company',options = ('Apex','Apple','Google'))
st.write("Check out for more company details: [link](https://eoddata.com/symbols.aspx)")
tickerSymb_dict = {'Apex':'A', 'Apple':'AAPL', 'Google':'GOOGL'}
tickerSymb = tickerSymb_dict[selectOptions]

if start_date >= end_date:
    st.error("Correct the date selection")
else:
    st.write("""Shown are the stock closing price and volume of the company """, selectOptions, """whose Ticker is""",tickerSymb)

tickerData = yf.Ticker(tickerSymb)
tickerDF = tickerData.history(period='1d', start=start_date, end=end_date)

if len(tickerDF) == 0:
    st.error("No Data Present for the selected date range")
elif len(tickerDF) == 1:
    tickerDF
    st.write("""
    ###### Single set of data present, cannot be shown on the chart
    """)
else:
    st.write(""" ### Closing Line Chart""")
    st.line_chart(tickerDF.Close)
    st.write(""" ### Volume Line Chart""")
    st.line_chart(tickerDF.Volume)