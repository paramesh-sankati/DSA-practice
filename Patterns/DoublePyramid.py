n=6
m=n//2
for i in range(1,m+1):
    for j in range(1,m+(i-1)+1):
        if j<=m-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(1,m+1):
    for j in range(1,m*2-i+1):
        if j<=i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
