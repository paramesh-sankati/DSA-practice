n=5
c=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end=" ")
        else:
            if c>10:
                print(" ",end="")
            print(c,end=" ")
            c+=1
    print()
        
  