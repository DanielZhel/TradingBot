import talib as tl
import numpy as np
def get_stoch_values(inst_data):
    a = tl.STOCH(np.array(inst_data['high']),np.array(inst_data['low']), np.array(inst_data['close']))
    K = a[0]
    D = a[1]
    T = inst_data['time']
    return K,D,T
def get_macd_values(inst_data):
    a = tl.MACD(np.array(inst_data['close']))
    T = inst_data['time']
    return a, T

def get_ema_values(inst_data, period):
    a = tl.EMA(np.array(inst_data['close']), period)
    T = inst_data['time']
    return a, period, T