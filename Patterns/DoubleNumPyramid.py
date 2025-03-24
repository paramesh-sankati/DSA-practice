n=7
m=n//2+1
c=1
for i in range(1,m+1):
    for j in range(1,m+i):
        if j<=m-i:
            print(" ",end=" ")
        else:
            print(i,end=" ")
            c=i
    print()
for i in range(1,m):
    for j in range(1,m*2-i):
        if j<=i:
            print(" ",end=" ")
        else:
            print(c+1,end=" ")
    c+=1
    print()
    