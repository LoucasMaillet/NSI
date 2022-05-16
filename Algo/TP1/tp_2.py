
def give(value: int, sys : tuple) -> list: 
    given = []
    i = m = 0
    max_i = len(sys)
    for v in sys:
        if value <= 0: break
        elif v > value: continue
        n = value // v
        value -= n * v
        given.append((n,  v))
        m+=1
    return given, m

    
value = 21
sys = (500, 200, 100, 50, 20, 10, 2, 1)

print(give(value, sys))

def moreUsed(value : int, sys : tuple) -> list:
    max_m = 0
    max_list = []
    for i in range(value):
        m = give(i, sys)[1]
        if m > max_m:
            max_m = m
        else m == max_m:
            max_list = 
    return used.items()
    
print(moreUsed(200, sys))
