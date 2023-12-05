def reduce_repeat(crossZone):
    j=1
    i=0
    delete =[]
    while i < len(crossZone)-1:
        while j < len(crossZone):
            if(crossZone[i][3]==crossZone[j][3]):
                delete.append(i)
            j=j+1
        i=i+1
    for x in range(len(delete)):
        crossZone.pop(delete[x])
    return crossZone

