import ChartsInit as init
import Data as data
import Indicators as indicators
import GetStat as gs
from tkinter import messagebox as mb

def bot_start(inst_list,
              first_timeframe,
              second_timeframe,
              ema_period,
              high_stoch_level,
              low_stoch_level,
              up_range_ema,
              lo_range_ema,
              risk,
              high_stop_percent,
              low_stop_percent,
              min_stop_percent):
    statistic=[]
    for i in range(len(inst_list)):
        inst_data1= data.get_instrument_data(inst_list[i],first_timeframe, 100)
        inst_data2= data.get_instrument_data(inst_list[i],second_timeframe, 300)
        ema_values= indicators.get_ema_values(inst_data1,ema_period)
        macd_values= indicators.get_macd_values(inst_data1)
        stoch_values= indicators.get_stoch_values(inst_data2)
        stat=init.charts_init(inst_data1, 
                        inst_data2, 
                        macd_values, 
                        ema_values, 
                        stoch_values, 
                        i, 
                        inst_list, 
                        first_timeframe, 
                        second_timeframe,
                        high_stoch_level,
                        low_stoch_level,
                        up_range_ema,
                        lo_range_ema,
                        risk, 
                        inst_list[i],
                        high_stop_percent,
                        low_stop_percent,
                        min_stop_percent)
        statistic = statistic+stat[0]+stat[1]
    winrate=  gs.get_statistic(statistic)   
    
    mb.showinfo("Statistics", f"Winrate: {winrate}% \n Number of trades: {len(statistic)} \n FirstTF: {first_timeframe} \n SecondTF: {second_timeframe} \n High stoch level: {high_stoch_level}% \n Low stoch level: {low_stoch_level}% \n Upper ema range: {up_range_ema}% \n Lower ema rane: {lo_range_ema}% \n Risk: {risk}")
  

