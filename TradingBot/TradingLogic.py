import ReduceRepeat as rr
import Indicators as ind

# Метод рассчитывает зоны и стоп для шорта МАКД и стохаст
def get_short_entry_zone_macd(instData1,instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    emaValues = ind.GetEMAValues(instData1,26)
    short_entry = []
    # Все значения МАКД
    for j in range (len(macdValues[0][0])-1):
        for i in range(len(stochValues[0])):
            # Условие для МАКД
            if (macdValues[0][1][j]<0 and macdValues[0][1][j]>macdValues[0][0][j]): 
                # Условие для проверки присутствия стохаста в интервале МАКД
                if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
                    # Условие для стохаста
                    if (stochValues[0][i-1] > 80 and stochValues[0][i] < stochValues[1][i] and stochValues[0][i-1]>stochValues[1][i-1]):
                        fast = float(stochValues[0][i])
                        slow = float(stochValues[1][i])
                        time = stochValues[2][i]
                        entry_price = float(instData2['open'][i])
                        stopt = float(max(instData2['high'][i-4], 
                                             instData2['high'][i],
                                             instData2['high'][i-1],
                                             instData2['high'][i-2],
                                             instData2['high'][i-3]))
                        stoplength = []
                        stop =[]
                        # Добавление цены и времени для отображения линии стопа
                        for j in range(10):
                            stoplength.append(instData2['time'][i+j])
                            stop.append(stopt)
                            
                        a = [entry_price,fast,slow,time,stop, stoplength]
                        short_entry.append(a)  
    # Устранение повторений                    
    short_entry = rr.reduce_repeat(short_entry)              
    return short_entry

# Метод рассчитывает зоны и стоп для лонга МАКД и стохаст
def get_long_entry_zone_macd(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    long_entry = []
     # Все значения МАКД
    for j in range (len(macdValues[0][0])-1):
        for i in range(len(stochValues[0])):
            # Условие для МАКД
            if (macdValues[0][1][j]>0 and macdValues[0][1][j]>macdValues[0][0][j]):
                # Условие для проверки присутствия стохаста в интервале МАКД
                if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
                    # Условие для стохаста
                    if (stochValues[0][i] < 20 and stochValues[0][i] > stochValues[1][i] and  stochValues[0][i-1]<stochValues[1][i-1]):
                        fast = float(stochValues[0][i+1])
                        slow = float(stochValues[1][i+1])
                        time = stochValues[2][i]
                        entry_price = float(instData2['open'][i])
                        stopt = float(min(instData2['low'][i-4], 
                                         instData2['low'][i],
                                         instData2['low'][i-1],
                                         instData2['low'][i-2],
                                         instData2['low'][i-3]))
                        stoplength = []
                        stop =[]
                        # Добавление цены и времени для отображения линии стопа
                        for j in range(10):
                            stoplength.append(instData2['time'][i+j])
                            stop.append(stopt)
                           
                        a = [entry_price,fast,slow,time,stop,stoplength]
                        long_entry.append(a)
    # Устранение повторений
    long_entry = rr.reduce_repeat(long_entry)
    return long_entry

# Метод рассчитывает зоны и стоп для лонга ЕМА и стохаст
def get_long_entry_zone_ema(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    emaValues =  ind.GetEMAValues(instData1,26)
    long_entry = []
    
    # Все значения ЕМА
    # 0.009 - процент нахождения цены от ЕМА
    for j in range (len(emaValues[0])-1):
        emaMin = emaValues[0][j]-emaValues[0][j]*0.009
        emaMax = emaValues[0][j]+emaValues[0][j]*0.009
        for i in range(len(stochValues[0])):
            # Проверка нахождения цены в интервале от ЕМА до ЕМА+%
            if (emaValues[0][j]<=instData2['open'][i]<=emaMax):
                # Условие для проверки присутствия стохаста в интервале ЕМА
                if(emaValues[2][j-1]<=stochValues[2][i]<=emaValues[2][j+1]):
                    # Условие для стохаста
                    if (stochValues[0][i] < 20 and stochValues[0][i] > stochValues[1][i] and  stochValues[0][i-1]<stochValues[1][i-1]):
                        fast = float(stochValues[0][i+1])
                        slow = float(stochValues[1][i+1])
                        time = stochValues[2][i]
                        entry_price = float(instData2['open'][i])
                        stopt = float(min(instData2['low'][i-4], 
                                         instData2['low'][i],
                                         instData2['low'][i-1],
                                         instData2['low'][i-2],
                                         instData2['low'][i-3]))
                        stoplength = []
                        stop =[]
                        # Добавление цены и времени для отображения линии стопа
                        for j in range(10):
                            stoplength.append(instData2['time'][i+j])
                            stop.append(stopt)
                           
                        a = [entry_price,fast,slow,time,stop,stoplength]
                        long_entry.append(a)
    # Устранение повторений
    long_entry = rr.reduce_repeat(long_entry)
    return long_entry

# Метод рассчитывает зоны и стоп для шорта ЕМА и стохаст
def get_short_entry_zone_ema(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    emaValues =  ind.GetEMAValues(instData1,26)
    short_entry = []
    # Все значения ЕМА
    for j in range (len(emaValues[0])-1):
        emaMin = emaValues[0][j]-emaValues[0][j]*0.003
        emaMax = emaValues[0][j]+emaValues[0][j]*0.003
        for i in range(len(stochValues[0])):
            # Проверка нахождения цены в интервале от ЕМА до ЕМА-%
            if (emaMin<=instData2['open'][i]<=emaValues[0][j] ):
                # Условие для проверки присутствия стохаста в интервале ЕМА
                if(emaValues[2][j-1]<=stochValues[2][i]<=emaValues[2][j+1]):
                    # Условие для стохаста
                    if (stochValues[0][i-1] > 80 and stochValues[0][i] < stochValues[1][i] and stochValues[0][i-1]>stochValues[1][i-1]):
                        fast = float(stochValues[0][i+1])
                        slow = float(stochValues[1][i+1])
                        time = stochValues[2][i]
                        entry_price = float(instData2['open'][i])
                        stopt = float(max(instData2['high'][i-4], 
                                         instData2['high'][i],
                                         instData2['high'][i-1],
                                         instData2['high'][i-2],
                                         instData2['high'][i-3]))
                        stoplength = []
                        stop =[]
                        # Добавление цены и времени для отображения линии стопа
                        for j in range(10):
                            stoplength.append(instData2['time'][i+j])
                            stop.append(stopt)
                            
                        a = [entry_price,fast,slow,time,stop, stoplength]
                        short_entry.append(a)  
    # Устранение повторений                    
    short_entry = rr.reduce_repeat(short_entry)              
    return short_entry

# Метод рассчитывает зоны и стоп для шорта ЕМА МАКД и стохаст    
def get_short_entry_zone_macdema(instData1,instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    emaValues = ind.GetEMAValues(instData1,26)
    short_entry = []
    # Все значения МАКД
    for j in range (len(macdValues[0][0])-1):
        emaMin = emaValues[0][j]-emaValues[0][j]*0.009
        emaMax = emaValues[0][j]+emaValues[0][j]*0.003
            
        for i in range(len(stochValues[0])):
            # Проверка нахождения цены в интервале от ЕМА до ЕМА-%
            if (emaMin<=instData2['open'][i]<=emaValues[0][j] ):
                # Условие для МАКД
                if (macdValues[0][1][j]<0 and macdValues[0][1][j]>macdValues[0][0][j]):  
                    # Условие для проверки присутствия стохаста в интервале МАКД
                    if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
                        # Условие для стохаста
                        if (stochValues[0][i-1] > 80 and stochValues[0][i] < stochValues[1][i] and stochValues[0][i-1]>stochValues[1][i-1]):
                            fast = float(stochValues[0][i+1])
                            slow = float(stochValues[1][i+1])
                            time = stochValues[2][i]
                            entry_price = float(instData2['open'][i])
                            stopt = float(max(instData2['high'][i-4], 
                                             instData2['high'][i],
                                             instData2['high'][i-1],
                                             instData2['high'][i-2],
                                             instData2['high'][i-3]))
                            stoplength = []
                            stop =[]
                            # Добавление цены и времени для отображения линии стопа
                            for j in range(10):
                                stoplength.append(instData2['time'][i+j])
                                stop.append(stopt)
                            
                            a = [entry_price,fast,slow,time,stop, stoplength]
                            short_entry.append(a)  
    # Устранение повторений                        
    short_entry = rr.reduce_repeat(short_entry)              
    return short_entry    

# Метод рассчитывает зоны и стоп для лонга ЕМА МАКД и стохаст
def get_long_entry_zone_macdema(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    emaValues = ind.GetEMAValues(instData1,26)
    long_entry = []
    # Все значения МАКД
    for j in range (len(macdValues[0][0])-1):
        emaMin = emaValues[0][j]-emaValues[0][j]*0.003
        emaMax = emaValues[0][j]+emaValues[0][j]*0.003
        for i in range(len(stochValues[0])):
            # Проверка нахождения цены в интервале от ЕМА до ЕМА+%
            if (emaValues[0][j]<=instData2['open'][i]<=emaMax):
                # Условие для МАКД
                if (macdValues[0][1][j]>0 and macdValues[0][1][j]>macdValues[0][0][j]):
                    # Условие для проверки присутствия стохаста в интервале МАКД
                    if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
                        # Условие для стохаста
                        if (stochValues[0][i] < 20 and stochValues[0][i] > stochValues[1][i] and  stochValues[0][i-1]<stochValues[1][i-1]):
                            fast = float(stochValues[0][i+1])
                            slow = float(stochValues[1][i+1])
                            time = stochValues[2][i]
                            entry_price = float(instData2['open'][i])
                            stopt = float(min(instData2['low'][i-4], 
                                             instData2['low'][i],
                                             instData2['low'][i-1],
                                             instData2['low'][i-2],
                                             instData2['low'][i-3]))
                            stoplength = []
                            stop =[]
                            # Добавление цены и времени для отображения линии стопа
                            for j in range(10):
                                stoplength.append(instData2['time'][i+j])
                                stop.append(stopt)
                           
                            a = [entry_price,fast,slow,time,stop,stoplength]
                            long_entry.append(a)
    # Устранение повторений                        
    long_entry = rr.reduce_repeat(long_entry)
    return long_entry  

# Метод строит на графике точки входа и стоп для шорта
def get_short_Signal(instData1, instData2,fig, go):
    short_entry = get_short_entry_zone_macdema(instData1, instData2)
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


# Метод строит на графике точки входа и стоп для лонга        
def get_long_Signal(instData1,instData2,fig,go):
    long_entry = get_long_entry_zone_macdema(instData1, instData2)
    for i in range(len(long_entry)):
        fig.add_trace(go.Scatter(
            x=[long_entry[i][3]],
            y=[long_entry[i][0]],
            mode = "markers",
            marker_symbol="arrow-up",
            marker_size=7,
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
    
    

