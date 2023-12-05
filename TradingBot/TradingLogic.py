import ReduceRepeat as rr
import Indicators as ind
def get_Over_Cross_Zone(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    overCross = []
    for j in range (len(macdValues[0][0])-1):
        for i in range(len(stochValues[0])):
            if ( macdValues[0][1][j]>macdValues[0][0][j]):    
                if(macdValues[1][j-1]<=stochValues[2][i]<=macdValues[1][j+1]):
                    if (stochValues[0][i] > 80 and stochValues[0][i] < stochValues[1][i]):
                        fast = float(stochValues[0][i])
                        slow = float(stochValues[1][i])
                        time = stochValues[2][i]
                        high = float(instData2['high'][i])
                        a = [high,fast,slow,time]
                        overCross.append(a)  
    overCross = rr.reduce_repeat(overCross)
                      
    return overCross

def get_Less_Cross_Zone(instData1, instData2):
    stochValues = ind.GetStochValues(instData2)
    macdValues =  ind.GetMACDValues(instData1)
    lessCross = []
    for j in range (len(macdValues[0][0])-1):
        if ( macdValues[0][1][j]>macdValues[0][0][j]):
            for i in range(len(stochValues[0])):
                if(macdValues[1][j-1]<stochValues[2][i]<macdValues[1][j+1]):
                    if (stochValues[0][i] < 20 and stochValues[0][i] > stochValues[1][i]):
                        fast = float(stochValues[0][i])
                        slow = float(stochValues[1][i])
                        time = stochValues[2][i]
                        low = float(instData2['low'][i])
                        a = [low,fast,slow,time]
                        lessCross.append(a)
    lessCross = rr.reduce_repeat(lessCross)
    return lessCross
    
# def get_Long_Signal(instData1, instData2, matplotlib):
#     crossLess = get_Less_Cross_Zone(instData1, instData2)
#     for i in range(len(instData2)):
#         for j in range(len(crossLess)):
#             if(instData2.loc[i, 'Time'] == crossLess[j][2]):
#                 matplotlib.pyplot.scatter(i,instData2.loc[i, 'Low'],c="black",marker='d')
                
# def get_Short_Signal(instData1, instData2, matplotlib):                
#     crossOver = get_Over_Cross_Zone(instData1, instData2)
#     for i in range(len(instData2)):
#         for j in range(len(crossOver)):
#             if(instData2.loc[i, 'Time'] == crossOver[j][2]):
#                 matplotlib.pyplot.scatter(i,instData2.loc[i, 'High'],c="black",marker='d')

def get_short_Signal(instData1, instData2,fig, go):
    overCross = get_Over_Cross_Zone(instData1, instData2)
    for i in range(len(overCross)):
        fig.add_trace(go.Scatter(
            x=[overCross[i][3]],
            y=[overCross[i][0]],
            mode = "markers",
            marker_symbol="diamond-dot",
            marker_size=13,
            marker_line_width=2,
            marker_line_color ="red"
            ), 
            row=1,
            col=2
        )
def get_long_Signal(instData1, instData2,fig, go):
    lessCross = get_Less_Cross_Zone(instData1, instData2)
    for i in range(len(lessCross)):
        fig.add_trace(go.Scatter(
            x=[lessCross[i][3]],
            y=[lessCross[i][0]],
            mode = "markers",
            marker_symbol="diamond-dot",
            marker_size=13,
            marker_line_width=2,
            marker_line_color ="green"
            ), 
            row=1,
            col=2
        )


