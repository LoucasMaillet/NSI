def sortedByWeight(items : list) -> list:
    return sorted(items, key= lambda item: item[1], reverse= True)

def sortedByPrice(items : list) -> list:
    return sorted(items, key= lambda item: item[2], reverse= True)

def sortedByWeightPrice(items : list) -> list:
    return sorted(items, key= lambda item: item[1] / item[2])

def fillLight(weight: int, items : list) -> list:
    res = []
    i = 0
    max_i = len(items)
    while 0 < weight and i < max_i:
        [k, w, *_] = items[i]
        if(w > weight):
             i+=1
             continue
        weight -= w
        res.append(k)
    return res

def fillLightSet(weight: int, items : list) -> set:
    res = set()
    for [k, w, *_] in items:
        if (weight < w): 
            if (weight == 0): break
            else: continue
        weight -= w
        res.add(k)
    #i = 0
    #max_i = len(items)
    #while 0 < weight and i < max_i:
    #    [k, w, *_] = items[i]
    #    if(w > weight): continue
    #    weight -= w
    #    res.append(k)
    #    i += 1
    return res

w = 50
T2= [('A',48,400),('B',30,290),('C',30,280),('D',10,140),('E',10,140),
     ('F',10,140),('G',10,140),('H',10,140),('I',2,35),('J',2,20),
     ('K',2,20),('L',2,10),('M',1,15),('N',1,15),('O',1,15),
     ]

print("\nSorted by weight\n")
print(fillLight(w, sortedByWeight(T2)))
print(fillLightSet(w, sortedByWeight(T2)))

print("\nSorted by price\n")
print(fillLight(w, sortedByPrice(T2)))
print(fillLightSet(w, sortedByPrice(T2)))

print("\nSorted by weight's price\n")
print(fillLight(w, sortedByWeightPrice(T2)))
print(fillLightSet(w, sortedByWeightPrice(T2)))