s='AZGB'
#print(ord(start)-39)
def clockwise(st,en):
    if st<en:
        return en-st
    else:
        return (26-st)+en
    
def anticlock(st,en):
    if st>en:
        return st-en
    else:
        return (26-en)+st
    
def min_time(s):
    minimum_time=0
    for i in range(len(s)-1):
        start,end=ord(s[i])-39,ord(s[i+1])-39
        clock_wise_time=clockwise(start,end)
        anticlock_wise_time=anticlock(start,end)
        minimum_time+=min(clock_wise_time,anticlock_wise_time)
    return minimum_time

print(min_time(s))