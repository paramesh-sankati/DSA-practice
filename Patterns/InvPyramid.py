n=5
for i in range(1,n+1):
    for j in range(1,n*2-i+1):
        if j<=i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")    
    print()