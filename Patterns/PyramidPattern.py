n=5
for i in range(n):
    for j in range(1,n+i+1):
        if i+j<=n-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
    