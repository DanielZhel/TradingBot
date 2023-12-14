def get_statistic(stat):
    pos_positions=[]
    if (len(stat) != 0):
        for i in range(len(stat)):
            if(stat[i]==1):
                pos_positions.append(stat[i])
        winrate=(len(pos_positions)/len(stat))*100
        return round(winrate,2)




