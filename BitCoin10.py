# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:45:38 2019

@author: Jeffrey
"""
""" Be sure to download this papckage first.... pip install cryptocompare   """


import cryptocompare

import pandas as pd

#df = pd.DataFrame


#Gathers all the prices and prints themin thier top 20 rank from 5/16/19


print("Below are the top 20 coins according to Coinbase...")
BTC = cryptocompare.get_price('BTC',curr='USD',full=False)

print('1: ', BTC)

ETH = cryptocompare.get_price('ETH',curr='USD',full=False)

print('2: ', ETH)

XRP = cryptocompare.get_price('XRP',curr='USD',full=False)

print('3: ', XRP)


BCH = cryptocompare.get_price('BCH',curr='USD',full=False)

print('4: ', BCH)

LTC = cryptocompare.get_price('LTC',curr='USD',full=False)

print('5: ', LTC)

XLM = cryptocompare.get_price('XLM',curr='USD',full=False)

print('6: ', XLM)

ETC = cryptocompare.get_price('ETC',curr='USD',full=False)

print('7: ', ETC)

USDC = cryptocompare.get_price('USDC',curr='USD',full=False)

print('8: ', USDC)

REP = cryptocompare.get_price('REP',curr='USD',full=False)

print('9: ', REP)

ZRX = cryptocompare.get_price('ZRX',curr='USD',full=False)

print('10: ',ZRX)


#Function that fetches coin of choice in realtime...
def getcoin(coin):
    while coin != "Exit":
        getcoin = cryptocompare.get_price(coin,curr='USD',full=False)
        print(getcoin)
        coin = input("Input the coin you would like in realtime or enter Exit: ")
    else:
        print("Terminating Program...")

coin = input("Input coin you would like in realtime or input 'Exit': ")
getcoin(coin)

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