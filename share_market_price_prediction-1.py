# packages
import pandas as pd
import numpy as np
import sklearn
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Prediction Function

def price_prediction(year,month,day,companies,Open,High,Low,Adj_Close,Volume,
                     Market_Cap,PE_Ratio,Beta,EPS,Forward_PE,Net_Income,Debt_to_Equity,
                     Return_on_Equity,Current_Ratio,Dividends_Paid,Dividend_Yield,
                     Quarterly_Revenue_Growth,Target_Price,Free_Cash_Flow,Operating_Margin,
                     Profit_Margin,Quick_Ratio,Price_to_Book_Ratio,Enterprise_Value,
                     Total_Debt,Annual_Dividend_Rate):
    
    Dividend = Market_Cap/Volume

    if companies == "Amazon":
        Am, Ap, Fa, Go, Ne = (1, 0, 0, 0, 0)
    elif companies == "Apple":
        Am, Ap, Fa, Go, Ne = (0, 1, 0, 0, 0)
    elif companies == "Facebook":
        Am, Ap, Fa, Go, Ne = (0, 0, 1, 0, 0)
    elif companies == "Google":
        Am, Ap, Fa, Go, Ne = (0, 0, 0, 1, 0)
    elif companies == "Netflix":
        Am, Ap, Fa, Go, Ne = (0, 0, 0, 0, 1)

    with open("Model_2.pkl","rb") as f:
        model = pickle.load(f)

    user_data = np.array([[year,month,day,Open,High,Low,Adj_Close,Volume,
                     Market_Cap,PE_Ratio,Beta,EPS,Forward_PE,Net_Income,Debt_to_Equity,
                     Return_on_Equity,Current_Ratio,Dividends_Paid,Dividend_Yield,
                     Quarterly_Revenue_Growth,Target_Price,Free_Cash_Flow,Operating_Margin,
                     Profit_Margin,Quick_Ratio,Price_to_Book_Ratio,Enterprise_Value,
                     Total_Debt,Annual_Dividend_Rate,Am, Ap, Fa, Go, Ne, Dividend]])
    
    y_pred = model.predict(user_data)
    st.write("## :green[The Predicted Amount is: ]",round(y_pred[0],3))



# Streamlit Part
st.set_page_config(layout= "wide")
st.title("SHARE MARKET PRICE PREDICTION")
with st.sidebar:
    select = option_menu("Main Menu",["Share Market", "Prediction", "About"])

if select == "Share Market":

    "The Share Market Explained"
    "The share market, or stock market, is a platform where investors buy and sell shares of publicly traded companies. It connects businesses seeking capital with individuals and institutions looking to invest, contributing to economic growth."
    "What Are Shares?"
    "Shares represent ownership in a company. When you buy shares, you become a partial owner of that company, entitled to a portion of its profits and potential capital gains."
    "Key Components of the Share Market :"
    "1) Stock Exchanges: Platforms like the New York Stock Exchange (NYSE), NASDAQ, and National Stock Exchange (NSE) facilitate buying and selling shares."
    "2) Stock Indices: Indices such as the S&P 500, Dow Jones, and Nifty 50 track the performance of a group of stocks, providing a snapshot of the market’s overall health."
    "3) Brokers: Licensed intermediaries who facilitate transactions between buyers and sellers."
    "  How Does It Work? "

    "Buyers and Sellers: Investors place orders to buy or sell shares through brokers or trading platforms."
    "4) Orders: A market order buys or sells shares at the best available price, while a limit order sets a specific price at which you want to buy or sell."
    "5) Trading Hours: The market operates during set hours, typically Monday to Friday."
    " Benefits of Investing in the Share Market:"
    "1) Capital Appreciation: Potential for your investment to grow as share prices rise."
    "2) Dividends: Some companies distribute a portion of their profits to shareholders as dividends."
    "3) Diversification: Spread your investments across different industries to reduce risk."

    "Risks to Consider:"
    "I) Market Risk: Prices can fluctuate due to economic conditions, company performance, or global events."
    "II) Volatility: The stock market can experience rapid and significant price movements."
    "III) Liquidity Risk: Shares may be difficult to sell if there is low market demand."

    "Why Invest in the Share Market?"
    "Investing in the share market provides opportunities for long-term wealth creation, passive income through dividends, and the ability to support innovative companies. However, it's important to understand the risks and make informed investment decisions. what shares are to how it works and the benefits and risks of investing. It’s ideal for introducing newcomers to the world of stocks!"
    
if select == "Prediction":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # Year
        year = st.selectbox("Select the Year",[i for i in range(2005,2051)])
        # Month
        month = st.selectbox("Select the Month",[i for i in range(1,13)])
        # Day
        day = st.selectbox("Select the Day",[i for i in range(1,32)])
         # List of companies
        companies =st.selectbox("Select of Companies",["Amazon", "Apple", "Facebook", "Google", "Netflix"])    
        Open = st.number_input('Enter the open price ',  min_value=0.0, step=0.1, format="%f")
        High = st.number_input('Enter the High price ',  min_value=0.0, step=0.1, format="%f")
        Low= st.number_input('Enter the Low price ',  min_value=0.0, step=0.1, format="%f")
        Adj_Close= st.number_input('Enter the Adj_Close price ',  min_value=0.0, step=0.1, format="%f")

    with col2:
       
        Volume = st.number_input('Enter the Volume value', min_value=0, step=1, format="%d")
        Market_Cap = st.number_input('Enter the Market_Cap  value ',  min_value=0.0, step=0.1, format="%f")
        PE_Ratio = st.number_input('Enter the PE_Ratio ',  min_value=0.0, step=0.1, format="%f")
        Beta = st.number_input('Enter the Beta ',  min_value=0.0, step=0.1, format="%f")
        EPS = st.number_input('Enter the EPS',  min_value=0.0, step=0.1, format="%f")
        Forward_PE = st.number_input('Enter the Forward_PE	',  min_value=0.0, step=0.1, format="%f")
        Net_Income = st.number_input('Enter the Net_Income	',  min_value=0.0, step=0.1, format="%f")
        Debt_to_Equity = st.number_input('Enter the Debt_to_Equity',  min_value=0.0, step=0.1, format="%f")



    with col3:
       
        Return_on_Equity = st.number_input('Enter the Return_on_Equity_(ROE)',  min_value=0.0, step=0.1, format="%f")
        Current_Ratio = st.number_input('Enter the Current_Ratio',  min_value=0.0, step=0.1, format="%f")
        Dividends_Paid = st.number_input('Enter the Dividends_Paid',  min_value=0.0, step=0.1, format="%f")
        Dividend_Yield = st.number_input('Enter the Dividend_Yield	',  min_value=0.0, step=0.1, format="%f")
        Quarterly_Revenue_Growth = st.number_input('Enter the Quarterly_Revenue_Growth',  min_value=0.0, step=0.1, format="%f")
        Target_Price = st.number_input('Enter the Target_Price',  min_value=0.0, step=0.1, format="%f")
        Free_Cash_Flow = st.number_input('Enter the Free_Cash_Flow', min_value=0, step=1, format="%d")
        Operating_Margin = st.number_input('Enter the Operating_Margin',  min_value=0.0, step=0.1, format="%f")


    with col4:
        
        Profit_Margin = st.number_input('Enter the Profit_Margin',  min_value=0.0, step=0.1, format="%f")
        Quick_Ratio = st.number_input('Enter the Quick_Ratio',  min_value=0.0, step=0.1, format="%f")
        Price_to_Book_Ratio = st.number_input('Enter the Price_to_Book_Ratio',  min_value=0.0, step=0.1, format="%f")
        Enterprise_Value = st.number_input('Enter the Enterprise Value',  min_value=0.0, step=0.1, format="%f")
        Total_Debt = st.number_input('Enter the Total_Debt',  min_value=0.0, step=0.1, format="%f")
        Annual_Dividend_Rate = st.number_input('Enter the Annual_Dividend_Rate',  min_value=0.0, step=0.1, format="%f")
        #Dividend = st.number_input('Enter the Dividend',  min_value=0.0, step=0.1, format="%f")

    button = st.button("Submit",use_container_width = True)
    if button:
        price_prediction(year,month,day,companies,Open,High,Low,Adj_Close,Volume,
                     Market_Cap,PE_Ratio,Beta,EPS,Forward_PE,Net_Income,Debt_to_Equity,
                     Return_on_Equity,Current_Ratio,Dividends_Paid,Dividend_Yield,
                     Quarterly_Revenue_Growth,Target_Price,Free_Cash_Flow,Operating_Margin,
                     Profit_Margin,Quick_Ratio,Price_to_Book_Ratio,Enterprise_Value,
                     Total_Debt,Annual_Dividend_Rate)
    
       