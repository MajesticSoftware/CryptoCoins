# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:35:35 2019

@author: Jeffrey
"""


import cryptocompare

import pandas as pd


#Gets just the value of each coin
def getvalue(coin):
    getvalue = cryptocompare.get_price(coin,curr='USD',full=False)
    getvalue = getvalue[coin].get('USD')
    print(getvalue)
    return getvalue


valueBTC = getvalue("BTC")
valueETH = getvalue("ETH")
valueXRP = getvalue("XRP")
valueBCH = getvalue("BCH")
valueLTC = getvalue("LTC")
valueXLM = getvalue("XLM")
valueETC = getvalue("ETC")
valueUSDC = getvalue("USDC")
valueREP = getvalue("REP")
valueZRX = getvalue("ZRX")
coindict = { "BTC":valueBTC,
              "ETH": valueETH,
              "XRP": valueXRP,
              "BCH": valueBCH,
              "LTC": valueLTC,
                "XLM": valueXLM,
                "ETC": valueETC,
                "USDC": valueUSDC,
                "REP": valueREP,
                "ZRX": valueZRX,
        }
col1 = ["BTC",
              "ETH",
              "XRP",
              "BCH",
              "LTC",
                "XLM",
                "ETC",
                "USDC",
                "REP",
                "ZRX"]
col2 = [valueBTC, 
valueETH,
valueXRP,
valueBCH,
valueLTC,
valueXLM,
valueETC,
valueUSDC, 
valueREP , valueZRX]
#print(col1)
#print(col2)
#print(coindict)
d = {"Coins": col1, "Values": col2}
#print(d)
df = pd.DataFrame(data = d)
print(df)