def reduce_repeat(crossZone):
    
    unique = []
    for zone in crossZone:
        if zone not in unique:
            unique.append(zone)
    print(unique)
    return unique

