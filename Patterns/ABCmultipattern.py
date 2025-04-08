n=4
r1=65
r2=99
for i in range(1,n+1):
    c1=65
    for j in range(1,n+1):
        if j<=i:
            print(chr(c1),end=" ")
            c1+=1
        else:
            print(" ",end=" ")
    c2=r1
    for j in range(1,n+1):
        if i+j>n:
            print(chr(c2),end=" ")
            c2-=1
        else:
            print(" ",end=" ")
    r1+=1
    print()
for i in range(1,(n-1)+1):
    c1=97
    for j in range(1,n+1):
        if i+j<=n:
            print(chr(c1),end=" ")
            c1+=1
        else:
            print(" ",end=" ")
    c2=r2
    for j in range(1,n+1):
        if j>i:
            print(chr(c2),end=" ")
            c2-=1
        else:
            print(" ",end=" ")
    r2-=1
    print()
