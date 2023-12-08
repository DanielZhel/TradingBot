import talib
import numpy as np

def GetStochValues(instData):
    a = talib.STOCH(np.array(instData['high']),np.array(instData['low']), np.array(instData['close']))
    K = a[0]
    D = a[1]
    T = instData['time']
    return K,D,T

def GetMACDValues(instData):
    a = talib.MACD(np.array(instData['close']))
    T = instData['time']
    return a, T

def GetEMAValues(instData, period):
    a = talib.EMA(np.array(instData['close']), period)
    T = instData['time']
    return a, period, T