import yfinance as yf
import pandas as pd

def obter_dados(empresa, ticker):
    data = yf.Ticker(ticker)
    hist = data.history(period="5y", interval="5d")
    hist.reset_index(inplace=True)  
    hist['SMA'] = hist['Close'].rolling(window=10).mean()
    hist['EMA'] = hist['Close'].ewm(span=10, adjust=False).mean()
    hist['Empresa'] = empresa  
    return hist