n=197
a=[int(i) for  i in str(n)]
s=0
while s<n:
    s=sum(a)
    if s==n:
        print("Keith Number")
        break
    a.pop(0)
    a.append(s)
else:
    print("Not a Keith Num")

    





