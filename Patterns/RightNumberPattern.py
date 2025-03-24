n=5
for i in range(1,n+1):
    c=1
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end=" ")
        else:
            print(c,end=" ")
            c+=1
    print()
