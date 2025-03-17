n=5
c=1
for i in range(n):
    for j in range(1,n+1):
        if j<=i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
            c+=1
    print()