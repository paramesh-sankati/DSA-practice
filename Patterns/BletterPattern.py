n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 and j==n or i==j==n or i==(n+1)//2 and j==n:
            print(" ",end=" ")
        elif i==n-4 or j==n-4 or i==n or j==n or i==(n+1)//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

