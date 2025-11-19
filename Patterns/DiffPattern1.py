n=5
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if i==1:
            if j==n or j==n+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if i==2:
            if j>=(2*n//2)-1 and j<=(2*n//2)+2:
                print("*",end=' ')
            else:
                print(" ",end=" ")
        if i>=3 and i<n:
            if i%2!=0:
                for k in range(i-1):
                    c=n+k
                    if j==c:
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
            else:
                for k in range(i):
                    c=n+k
                    if j==c:
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
      
    print()