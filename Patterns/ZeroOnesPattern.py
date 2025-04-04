n=6
c=0
for i in range(1,n+1):
    for j in range(1,i+1):
        if c==0:
            c+=1
            print(c,end=" ")
        else:
            c-=1
            print(c,end=" ")
    print()