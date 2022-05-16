def isPossible(stations_distance : list, r : int) -> bool:
    for d in stations_distance:
        if r < d: return False
    return True

def stopStation(stations_distance : list, r : int) -> list or str:
    
    if not isPossible(stations_distance, r): return "Imposible"
    
    i = 0
    r_stat = r
    station_i = []
    count = 0
    
    for d in stations_distance:
        count += 1
        if r_stat < d:
            r_stat = r
            station_i.append(i-1)
        r_stat -= d
        i += 1
    
    return station_i, count
    
stations_distance = [20 , 40 , 31 , 68 , 45 , 37 , 25 , 106 , 54 , 120 , 86 , 59]
r = 150

print(stopStation(stations_distance, r))

print(len(stations_distance))