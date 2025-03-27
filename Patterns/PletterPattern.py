n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n-4 or j==n-4 or i==(n+1)//2:
            print("*",end=" ")
        elif j==n and i<=(n+1)//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()