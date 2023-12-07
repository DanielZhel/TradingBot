import ReduceRepeat as rr
import Indicators as ind

def get_short_entry_zone(instData1,instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    short_entry = []
    for j in range (len(macdValues[0][0])-1):
        for i in range(len(stochValues[0])):
            if (macdValues[0][1][j]<0 and macdValues[0][1][j]>macdValues[0][0][j]):    
                if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
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
                        
                        for j in range(10):
                            stoplength.append(instData2['time'][i+j])
                            stop.append(stopt)
                            
                        a = [entry_price,fast,slow,time,stop, stoplength]
                        short_entry.append(a)  
    short_entry = rr.reduce_repeat(short_entry)
                      
    return short_entry

def get_long_enrty_zone(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    long_entry = []
    for j in range (len(macdValues[0][0])-1):
        for i in range(len(stochValues[0])):
            if (macdValues[0][1][j]>0 and macdValues[0][1][j]>macdValues[0][0][j]):
                if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
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
                        # Линия для стопа
                        for j in range(10):
                            stoplength.append(instData2['time'][i+j])
                            stop.append(stopt)
                           
                        a = [entry_price,fast,slow,time,stop,stoplength]
                        long_entry.append(a)
    long_entry = rr.reduce_repeat(long_entry)
    return long_entry

def get_short_Signal(instData1, instData2,fig, go):
    short_entry = get_short_entry_zone(instData1, instData2)
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
        
def get_long_Signal(instData1,instData2,fig,go):
    long_entry = get_long_enrty_zone(instData1, instData2)
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

# def get_long_exit(long_entry, instData2):
#     entryPrice=[]
    
    
    
    
    

