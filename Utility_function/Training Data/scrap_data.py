import sqlite3
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

def create_database_tabe():
    conn = sqlite3.connect('training_data.sqlite3')
    curs = conn.cursor()

    create_fin_table = """
    CREATE TABLE finSentiment (
    postDate DATE , 
    ticker varchar, 
    message_text varchar ,
    sentiment INT,
    label INT 
    )
    """
    curs.execute(create_fin_table)

    conn.commit()



create_database_tabe()

def get_news(ticker):
    url="http://finance.yahoo.com/rss/headline?s="
    symbol=ticker
    feed = requests.get(url+symbol)

    soup = BeautifulSoup(feed.text)

    news = soup.find_all('description')
    dates = soup.find_all('pubdate')
    text = []
    d = []

    for new in news[1:]:
        text.append(new.text)
    for date in dates:
        d.append(date.text)


    ticker_list = [ticker] *len(dates)
    dictionary = {"postDate": d,'ticker':ticker_list,"message_text": text, }

    df = pd.DataFrame(dictionary)

    return df

ticker="FB"

df = get_news(ticker)

print(df)

active_stock=["AMD","SNAP","NIO","CHK","GE","BAC","ECA","F","T","SFIX","CMCSA","MU","TSLA","GOLD",
              "SIRI","AAPL","PFE","RIG","MSFT","CIEN","CY","NLY","S","DWDP","KMI","NOK","VALE",
              "TWTR","HAL","WFC","GOLD","TEVA","RIG","FB","PBR","X","ATUS","S","VER","KO","UBER",
              "EBAY","MRVL","OXY","C","VZ","KHC","SLB","ORCL","MRO","NEM","SBUX","CUZ","BBD","ACB",
              "IQ","JPM","ROKU","QCOM","MPC","CY","ET","M","RF","CTVA","NRZ","SQ","JD","FDC","ZM",
              "CELG","WY","SYMC","XOM","HPE","KGC","GFI","NVDA","CLF","ZNGA","APC","HPQ","GPS","HBAN",
              "BX","TME","PG","CTL","JCI","GPK","CVS","WPX","FLEX","COG","NBL","SAN","KEY","CRM","STM",
              "MAT","MGM","WMB","SYF","DIS","V","MS","WMT","SCHW","BMY","ATVI","PVTL","GM","JNJ","MYL",
              "SFIX","AMAT","CIG","HST","GILD","AEO","KR","BMS","CIEN","INVH","BP","MRK","PYPL","WDC",
              "EXC","AMRN","IMMU","DVN","COTY","CVX","PCG","FITB","COP","TGT","ON","MO","D","MNST",
              "EQH","VIPS","BILI","FCX","INTC","BYND","DOCU","BSX","CSCO","ITUB","BABA"]

for stock in active_stock:
    df = get_news(stock)
    conn = sqlite3.connect('training_data.sqlite3')l..
    df.to_sql('finSentiment', con=conn,if_exists='append',index=False)
    conn.commit()