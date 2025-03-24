n=5
for i in range(1,n+1):
    c=1
    for j in range(1,n+i):
        if j<=n-i:
            print(" ",end=" ")
        else:
            if j>n:
                c=c-1
                print(c,end=" ") 
            else:
                print(c,end=" ")
                if c<i:
                    c+=1
                
    print()