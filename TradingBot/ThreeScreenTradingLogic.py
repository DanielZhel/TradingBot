import ReduceRepeat as rr
import PositionImit as pos
# Метод рассчитывает зоны и стоп для шорта МАКД и стохаст
# def get_short_entry_zone_macd(inst_data1,inst_data2, high_stoch_level, stoch_values,macd_values):
#     short_entry = []
#     # Все значения МАКД
#     for j in range (len(macd_values[0][0])-1):
#         for i in range(len(stoch_values[0])):
#             # Условие для МАКД
#             if (macd_values[0][1][j]<0 and macd_values[0][1][j]>macd_values[0][0][j]): 
#                 # Условие для проверки присутствия стохаста в интервале МАКД
#                 if(macd_values[1][j-1]<=stoch_values[2][i]<=macd_values[1][j+1]):
#                     # Условие для стохаста
#                     if (stoch_values[0][i-1] > high_stoch_level and stoch_values[0][i] < stoch_values[1][i] and stoch_values[0][i-1]>stoch_values[1][i-1]):
#                         fast = float(stoch_values[0][i])
#                         slow = float(stoch_values[1][i])
#                         time = stoch_values[2][i]
#                         entry_price = float(inst_data2['open'][i])
#                         stopt = float(max(inst_data2['high'][i-4], 
#                                              inst_data2['high'][i],
#                                              inst_data2['high'][i-1],
#                                              inst_data2['high'][i-2],
#                                              inst_data2['high'][i-3]))
#                         stop_length = []
#                         stop =[]
#                         # Добавление цены и времени для отображения линии стопа
#                         for j in range(10):
#                             stop_length.append(inst_data2['time'][i+j])
#                             stop.append(stopt)
                            
#                         a = [entry_price,fast,slow,time,stop, stop_length]
#                         short_entry.append(a)  
#     # Устранение повторений                    
#     short_entry = rr.reduce_repeat(short_entry)              
#     return short_entry

# # Метод рассчитывает зоны и стоп для лонга МАКД и стохаст
# def get_long_entry_zone_macd(inst_data1, inst_data2,low_stoch_level,stoch_values,macd_values):
#     long_entry = []
#      # Все значения МАКД
#     for j in range (len(macd_values[0][0])-1):
#         for i in range(len(stoch_values[0])):
#             # Условие для МАКД
#             if (macd_values[0][1][j]>0 and macd_values[0][1][j]>macd_values[0][0][j]):
#                 # Условие для проверки присутствия стохаста в интервале МАКД
#                 if(macd_values[1][j-1]<=stoch_values[2][i]<=macd_values[1][j+1]):
#                     # Условие для стохаста
#                     if (stoch_values[0][i] < low_stoch_level and stoch_values[0][i] > stoch_values[1][i] and  stoch_values[0][i-1]<stoch_values[1][i-1]):
#                         fast = float(stoch_values[0][i+1])
#                         slow = float(stoch_values[1][i+1])
#                         time = stoch_values[2][i]
#                         entry_price = float(inst_data2['open'][i])
#                         stopt = float(min(inst_data2['low'][i-4], 
#                                          inst_data2['low'][i],
#                                          inst_data2['low'][i-1],
#                                          inst_data2['low'][i-2],
#                                          inst_data2['low'][i-3]))
#                         stop_length = []
#                         stop =[]
#                         # Добавление цены и времени для отображения линии стопа
#                         for j in range(10):
#                             stop_length.append(inst_data2['time'][i+j])
#                             stop.append(stopt)
                           
#                         a = [entry_price,fast,slow,time,stop,stop_length]
#                         long_entry.append(a)
#     # Устранение повторений
#     long_entry = rr.reduce_repeat(long_entry)
#     return long_entry

# # Метод рассчитывает зоны и стоп для лонга ЕМА и стохаст
# def get_long_entry_zone_ema(inst_data1, inst_data2,low_stoch_level,up_range_ema,stoch_values, ema_values):
#     long_entry = []
    
#     # Все значения ЕМА
#     # 0.009 - процент нахождения цены от ЕМА
#     for j in range (len(ema_values[0])-1):
#         ema_min = ema_values[0][j]-ema_values[0][j]*0.009
#         ema_max = ema_values[0][j]+ema_values[0][j]*(up_range_ema/100)
#         for i in range(len(stoch_values[0])):
#             # Проверка нахождения цены в интервале от ЕМА до ЕМА+%
#             if (ema_values[0][j]<=inst_data2['open'][i]<=ema_max):
#                 # Условие для проверки присутствия стохаста в интервале ЕМА
#                 if(ema_values[2][j-1]<=stoch_values[2][i]<=ema_values[2][j+1]):
#                     # Условие для стохаста
#                     if (stoch_values[0][i] < low_stoch_level and stoch_values[0][i] > stoch_values[1][i] and  stoch_values[0][i-1]<stoch_values[1][i-1]):
#                         fast = float(stoch_values[0][i+1])
#                         slow = float(stoch_values[1][i+1])
#                         time = stoch_values[2][i]
#                         entry_price = float(inst_data2['open'][i])
#                         stopt = float(min(inst_data2['low'][i-4], 
#                                          inst_data2['low'][i],
#                                          inst_data2['low'][i-1],
#                                          inst_data2['low'][i-2],
#                                          inst_data2['low'][i-3]))
#                         stop_length = []
#                         stop =[]
#                         # Добавление цены и времени для отображения линии стопа
#                         for j in range(10):
#                             stop_length.append(inst_data2['time'][i+j])
#                             stop.append(stopt)
                           
#                         a = [entry_price,fast,slow,time,stop,stop_length]
#                         long_entry.append(a)
#     # Устранение повторений
#     long_entry = rr.reduce_repeat(long_entry)
#     return long_entry

# # Метод рассчитывает зоны и стоп для шорта ЕМА и стохаст
# def get_short_entry_zone_ema(inst_data1, inst_data2,high_stoch_level,lo_range_ema,stoch_values,  ema_values):
#     short_entry = []
#     # Все значения ЕМА
#     for j in range (len(ema_values[0])-1):
#         ema_min = ema_values[0][j]-ema_values[0][j]*(lo_range_ema/100)
#         # emaMax = emaValues[0][j]+emaValues[0][j]*(up_range_ema/100)
#         for i in range(len(stoch_values[0])):
#             # Проверка нахождения цены в интервале от ЕМА до ЕМА-%
#             if (ema_min<=inst_data2['open'][i]<=ema_values[0][j] ):
#                 # Условие для проверки присутствия стохаста в интервале ЕМА
#                 if(ema_values[2][j-1]<=stoch_values[2][i]<=ema_values[2][j+1]):
#                     # Условие для стохаста
#                     if (stoch_values[0][i-1] > high_stoch_level and stoch_values[0][i] < stoch_values[1][i] and stoch_values[0][i-1]>stoch_values[1][i-1]):
#                         fast = float(stoch_values[0][i+1])
#                         slow = float(stoch_values[1][i+1])
#                         time = stoch_values[2][i]
#                         entry_price = float(inst_data2['open'][i])
#                         stopt = float(max(inst_data2['high'][i-4], 
#                                          inst_data2['high'][i],
#                                          inst_data2['high'][i-1],
#                                          inst_data2['high'][i-2],
#                                          inst_data2['high'][i-3]))
#                         stop_length = []
#                         stop =[]
#                         # Добавление цены и времени для отображения линии стопа
#                         for j in range(10):
#                             stop_length.append(inst_data2['time'][i+j])
#                             stop.append(stopt)
                            
#                         a = [entry_price,fast,slow,time,stop, stop_length]
#                         short_entry.append(a)  
#     # Устранение повторений                    
#     short_entry = rr.reduce_repeat(short_entry)              
#     return short_entry

# Метод рассчитывает зоны и стоп для шорта ЕМА МАКД и стохаст    
def get_short_positions_macdema(inst_data2,
                                high_stoch_level,
                                lo_range_ema,
                                stoch_values,
                                macd_values,
                                ema_values,
                                high_stop_percent,
                                min_stop_percent):
    short_entry = []
    # Все значения МАКД
    for j in range (len(macd_values[0][0])-1):
        ema_min = ema_values[0][j]-ema_values[0][j]*(lo_range_ema/100)
        # ema_max = emaValues[0][j]+emaValues[0][j]*0.003
            
        for i in range(len(stoch_values[0])):
            # Проверка нахождения цены в интервале от ЕМА до ЕМА-%
            if (ema_min<=inst_data2['close'][i]<=ema_values[0][j] ):
                # Условие для МАКД
                if (macd_values[0][1][j]<=0 and macd_values[0][1][j]>macd_values[0][0][j]):  
                    # Условие для проверки присутствия стохаста в интервале МАКД
                    if(macd_values[1][j-1]<=stoch_values[2][i]<=macd_values[1][j+1]):
                        # Условие для стохаста
                        if (stoch_values[0][i-1] > high_stoch_level and stoch_values[0][i] < stoch_values[1][i] and stoch_values[0][i-1]>stoch_values[1][i-1]):
                            fast = float(stoch_values[0][i+1])
                            slow = float(stoch_values[1][i+1])
                            time = stoch_values[2][i]
                            entry_price = float(inst_data2['close'][i])
                            stopt = float(max(inst_data2['high'][i-4], 
                                             inst_data2['high'][i],
                                             inst_data2['high'][i-1],
                                             inst_data2['high'][i-2],
                                             inst_data2['high'][i-3]))
                            stop_length = []
                            stop =[]
                            stopt = stopt+(stopt*high_stop_percent/100)
                            if ((1-(entry_price/stopt))*100 > min_stop_percent):
                            # Добавление цены и времени для отображения линии стопа
                                for j in range(2):
                                    stop_length.append(inst_data2['time'][i+j])
                                    stop.append(stopt)
                            
                                a = [entry_price,fast,slow,time,stop, stop_length]
                                short_entry.append(a)  
    # Устранение повторений                        
    short_entry = rr.reduce_repeat(short_entry)              
    return short_entry    

# Метод рассчитывает зоны и стоп для лонга ЕМА МАКД и стохаст
def get_long_positions_macdema(inst_data2,
                               low_stoch_level, 
                               up_range_ema,
                               stoch_values, 
                               macd_values,
                               ema_values,
                               low_stop_percent,
                               min_stop_percent):
    long_entry = []
    # Все значения МАКД
    for j in range (len(macd_values[0][0])-1):
        # emaMin = emaValues[0][j]-emaValues[0][j]*0.003
        ema_max = ema_values[0][j]+ema_values[0][j]*(up_range_ema/100)
        for i in range(len(stoch_values[0])):
            # Проверка нахождения цены в интервале от ЕМА до ЕМА+%
            if (ema_values[0][j]<=inst_data2['close'][i]<=ema_max):
                # Условие для МАКД
                if (macd_values[0][1][j]>=0 and macd_values[0][1][j]>macd_values[0][0][j]):
                    # Условие для проверки присутствия стохаста в интервале МАКД
                    if(macd_values[1][j-1]<=stoch_values[2][i]<=macd_values[1][j+1]):
                        # Условие для стохаста
                        if (stoch_values[0][i] < low_stoch_level and stoch_values[0][i] > stoch_values[1][i] and  stoch_values[0][i-1]<stoch_values[1][i-1]):
                            fast = float(stoch_values[0][i+1])
                            slow = float(stoch_values[1][i+1])
                            time = stoch_values[2][i]
                            entry_price = float(inst_data2['close'][i])
                            stopt = float(min(inst_data2['low'][i-4], 
                                             inst_data2['low'][i],
                                             inst_data2['low'][i-1],
                                             inst_data2['low'][i-2],
                                             inst_data2['low'][i-3]))
                            stopt = stopt-(stopt*low_stop_percent/100)
                            stop_length = []
                            stop =[]
                            if ((1-(stopt/entry_price))*100 > min_stop_percent ):
                                for j in range(2):
                                    stop_length.append(inst_data2['time'][i+j])
                                    stop.append(stopt)
                           
                                a = [entry_price,fast,slow,time,stop,stop_length]
                                long_entry.append(a)    
                            # Добавление цены и времени для отображения линии стопа
                            
    # Устранение повторений                        
    long_entry = rr.reduce_repeat(long_entry)
    return long_entry  

# Метод строит на графике точки входа и стоп для шорта
def get_short_signal(inst_data2,
                     fig, 
                     go, 
                     high_stoch_value, 
                     lo_range_ema, 
                     stoch_values, 
                     macd_values, 
                     ema_values,
                     risk,
                     high_stop_percent,
                     min_stop_percent):
    short_entry = get_short_positions_macdema(inst_data2,
                                              high_stoch_value,
                                              lo_range_ema, 
                                              stoch_values, 
                                              macd_values, 
                                              ema_values,
                                              high_stop_percent,
                                              min_stop_percent)
    positions_stat = pos.get_short_position(short_entry, 
                                            inst_data2,risk)
    for i in range(len(short_entry)):
        fig.add_trace(go.Scatter(
            x=[short_entry[i][3]],
            y=[short_entry[i][0]],
            mode = "markers",
            marker_symbol="arrow-down",
            marker_size=7,
            marker_line_width=1,
            marker_line_color ="black",
            marker_color="red",name=f"Short{i}"
            ), 
            row=1,
            col=2
        )
        fig.add_trace(go.Scatter(
            x=short_entry[i][5],
            y=short_entry[i][4],
            mode='lines',
            name=f"Stop{i}",
            line=dict(color='darkred', width=2)
            ),
            row=1,
            col=2
        )
        for i in range(len(positions_stat[0])):
            fig.add_trace(go.Scatter(
                x=[positions_stat[0][i][1]],
                y=[positions_stat[0][i][0]],
                mode = "markers",
                marker_symbol="line-ew",
                marker_size=7,
                marker_line_width=1,
                marker_line_color ="black",
                marker_color="lightgreen", name=f"exit{i}"
            ), 
            row=1,
            col=2
        )
    return positions_stat[1]


# Метод строит на графике точки входа и стоп для лонга        
def get_long_signal(inst_data2,
                    fig,
                    go,
                    low_stoch_value,
                    up_range_ema, 
                    stoch_values, 
                    macd_values, 
                    ema_values,
                    risk,
                    low_stop_percent,
                    min_stop_percent):
    long_entry = get_long_positions_macdema(inst_data2,
                                            low_stoch_value,
                                            up_range_ema,
                                            stoch_values, 
                                            macd_values, 
                                            ema_values,
                                            low_stop_percent,
                                            min_stop_percent)
    positions_stat = pos.get_long_position(long_entry, inst_data2,risk)
    for i in range(len(long_entry)):
        fig.add_trace(go.Scatter(
            x=[long_entry[i][3]],
            y=[long_entry[i][0]],
            mode = "markers",
            marker_symbol="arrow-up",
            marker_size=10,
            marker_line_width=1,
            marker_line_color ="black",
            marker_color="lightgreen", name=f"Long{i}"
            ), 
            row=1,
            col=2
        )
        fig.add_trace(go.Scatter(
            x=long_entry[i][5],
            y=long_entry[i][4],
            mode='lines',
            name=f"Stop{i}",
            line=dict(color='darkred', width=2)
            ),
            row=1,
            col=2
        )
    for i in range(len(positions_stat[0])):
        fig.add_trace(go.Scatter(
            x=[positions_stat[0][i][1]],
            y=[positions_stat[0][i][0]],
            mode = "markers",
            marker_symbol="line-ew",
            marker_size=10,
            marker_line_width=1,
            marker_line_color ="black",
            marker_color="lightgreen", name=f"exit{i}"
            ), 
            row=1,
            col=2
        )
    return positions_stat[1]
            
    
    

