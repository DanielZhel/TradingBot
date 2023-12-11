from tkinter import Entry
from turtle import position
import ThreeScreenTradingLogic as tl
import Data as data
import Indicators as indicators




# inst_data1= data.get_instrument_data("XRP-USDT","2H", 100)
# inst_data2= data.get_instrument_data("XRP-USDT","30m", 300)
# ema_values= indicators.get_ema_values(inst_data1,26)
# macd_values= indicators.get_macd_values(inst_data1)
# stoch_values= indicators.get_stoch_values(inst_data2)

# long_entry=tl.get_long_entry_zone_macdema(inst_data1, inst_data2,30,5, stoch_values, macd_values, ema_values)      

def get_long_position(long_entry, inst_data2,risk):
    
    positions=[]
    pos_info = []
    if(len(long_entry)>0):
        for i in range(len(long_entry)):
            entry = long_entry[i][0]
            stop = long_entry[i][4][0]
            stop_percent= abs(100-(stop*100)/entry)
            take_percent = stop_percent*risk/100
            take = entry*take_percent + entry
            time = long_entry[i][3]
            a=[take, time, stop]
            pos_info.append(a)

    for i in range(len(pos_info)):        
        for j in range(len(inst_data2['time'])):
            if (pos_info[i][1]<inst_data2['time'][j]):
                if(inst_data2['low'][j]<pos_info[i][0]<inst_data2['high'][j]):
                    tp = pos_info[i][0]
                    tm = inst_data2['time'][j]
                    p = [tp,tm]
                    positions.append(p)
                    print("TakeProfit")
                    break
                elif(inst_data2['low'][j]<pos_info[i][2]<inst_data2['high'][j]):
                    sl = pos_info[i][2]
                    tm = inst_data2['time'][j]
                    p = [sl,tm]
                    print("Stop")
                    positions.append(p)
                    break
    return positions

def get_short_position(short_entry, inst_data2,risk):
    positions=[]
    pos_info = []
    if(len(short_entry)>0):
        for i in range(len(short_entry)):
            entry = short_entry[i][0]
            stop = short_entry[i][4][0]
            stop_percent= abs(100-(stop*100)/entry)
            take_percent = stop_percent*risk/100
            take = entry-entry*take_percent
            time = short_entry[i][3]
            a=[take, time, stop]
            pos_info.append(a)

    for i in range(len(pos_info)):        
        for j in range(len(inst_data2['time'])):
            if (pos_info[i][1]<inst_data2['time'][j]):
                if(inst_data2['low'][j]<pos_info[i][0]<inst_data2['high'][j]):
                    tp = pos_info[i][0]
                    tm = inst_data2['time'][j]
                    p = [tp,tm]
                    positions.append(p)
                    print("TakeProfit")
                    break
                elif(inst_data2['low'][j]<pos_info[i][2]<inst_data2['high'][j]):
                    sl = pos_info[i][2]
                    tm = inst_data2['time'][j]
                    p = [sl,tm]
                    print("Stop")
                    positions.append(p)
                    break
    return positions

    




