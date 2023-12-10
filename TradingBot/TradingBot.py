import ChartsInit as init
import Data as data
import Indicators as indicators

def bot_start(inst_list,frist_timeframe,second_timeframe,ema_period,high_stoch_level,low_stoch_level,up_range_ema,lo_range_ema):
  
    for i in range(len(inst_list)):
        inst_data1= data.get_instrument_data(inst_list[i],frist_timeframe, 100)
        inst_data2= data.get_instrument_data(inst_list[i],second_timeframe, 300)
        ema_values= indicators.get_ema_values(inst_data1,ema_period)
        macd_values= indicators.get_macd_values(inst_data1)
        stoch_values= indicators.get_stoch_values(inst_data2)
        init.charts_init(inst_data1, 
                        inst_data2, 
                        macd_values, 
                        ema_values, 
                        stoch_values, 
                        i, 
                        inst_list, 
                        frist_timeframe, 
                        second_timeframe,
                        high_stoch_level,
                        low_stoch_level,
                        up_range_ema,
                        lo_range_ema)
