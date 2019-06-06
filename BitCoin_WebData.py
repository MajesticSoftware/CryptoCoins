# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:45:38 2019

@author: Jeffrey
"""
""" Be sure to download this papckage first.... pip install cryptocompare   """


import cryptocompare



#Gathers all the prices and prints themin thier top 20 rank from 5/16/19


print("Below are the top 20 coins according to Coinbase...")
BTCprice = cryptocompare.get_price('BTC',curr='USD',full=False)

print('1: ', BTCprice)

ETHprice = cryptocompare.get_price('ETH',curr='USD',full=False)

print('2: ', ETHprice)

XRPprice = cryptocompare.get_price('XRP',curr='USD',full=False)

print('3: ', XRPprice)


BCHprice = cryptocompare.get_price('BCH',curr='USD',full=False)

print('4: ', BCHprice)

LTCprice = cryptocompare.get_price('LTC',curr='USD',full=False)

print('5: ', LTCprice)

XLMprice = cryptocompare.get_price('XLM',curr='USD',full=False)

print('6: ', XLMprice)

ETCprice = cryptocompare.get_price('ETC',curr='USD',full=False)

print('7: ', ETCprice)

USDCprice = cryptocompare.get_price('USDC',curr='USD',full=False)

print('8: ', USDCprice)

REPprice = cryptocompare.get_price('REP',curr='USD',full=False)

print('9: ', REPprice)

ZRXprice = cryptocompare.get_price('ZRX',curr='USD',full=False)

print('10: ',ZRXprice)

EOSprice = cryptocompare.get_price('EOS',curr='USD',full=False)

print('11: ', EOSprice)

BNBprice = cryptocompare.get_price('BNB',curr='USD',full=False)

print('12: ', BNBprice)

USDTprice = cryptocompare.get_price('USDT',curr='USD',full=False)

print('13: ', USDTprice)


ADAprice = cryptocompare.get_price('ADA',curr='USD',full=False)

print('14: ', ADAprice)


TRXprice = cryptocompare.get_price('TRX',curr='USD',full=False)

print('15: ', TRXprice)

XMRprice = cryptocompare.get_price('XMR',curr='USD',full=False)

print('16: ', XMRprice)

DASHprice = cryptocompare.get_price('DASH',curr='USD',full=False)

print('17: ', DASHprice)

IOTAprice = cryptocompare.get_price('IOTA',curr='USD',full=False)

print('18: ', IOTAprice)

BSVprice = cryptocompare.get_price('BSV',curr='USD',full=False)

print('19: ', BSVprice)

XTZprice = cryptocompare.get_price('XTZ',curr='USD',full=False)

print('20: ', XTZprice)

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
    
def getvalue(coin):
    getvalue = cryptocompare.get_price(coin,curr='USD',full=False)
    getvalue = getvalue[coin].get('USD')
    print(getvalue)

        
    