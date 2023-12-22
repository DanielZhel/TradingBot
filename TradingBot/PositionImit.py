def get_long_position(long_entry, inst_data2,risk):
    long_stat=[]
    positions=[]
    pos_info = []
    if(len(long_entry)>0):
        for i in range(len(long_entry)):
            entry = long_entry[i][0]
            stop = long_entry[i][4]
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
                    long_stat.append(1)
                    break
                elif(inst_data2['low'][j]<pos_info[i][2]<inst_data2['high'][j]):
                    sl = pos_info[i][2]
                    tm = inst_data2['time'][j]
                    p = [sl,tm]
                    long_stat.append(0)
                    positions.append(p)
                    break
    return positions, long_stat

def get_short_position(short_entry, inst_data2,risk):
    short_stat=[]
    positions=[]
    pos_info = []
    if(len(short_entry)>0):
        for i in range(len(short_entry)):
            entry = short_entry[i][0]
            stop = short_entry[i][4]
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
                    short_stat.append(1)
                    positions.append(p)
                    break
                elif(inst_data2['low'][j]<pos_info[i][2]<inst_data2['high'][j]):
                    sl = pos_info[i][2]
                    tm = inst_data2['time'][j]
                    p = [sl,tm]
                    short_stat.append(0)
                    positions.append(p)
                    break
    return positions, short_stat

    




