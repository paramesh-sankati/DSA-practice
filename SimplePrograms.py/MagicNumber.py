'''
Repeatedly sum the digits until you get a single digit. If it's 1, it's magic.
(e.g., 1729 → 1+7+2+9=19 → 1+9=10 → 1+0=1)
'''
n=50113
while n>=10:
    s1=str(n)
    sum1=sum([int(i) for i in str(n)])
    n=sum1
    if sum1==1:
        print("Magic Number")
        break
else:
    print("Not a Magic Number")
