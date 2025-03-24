n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end=" ")
        else:
            print(i,end=" ")
    for j in range(2,i+1):
        print(i,end=" ")
    print()
for i in range(2,n+1):
    c=3+i
    for j in range(1,n+1):
        if j<i:
            print(" ",end=" ")
        else:
            print(c,end=" ")
    for j in range(2,n-i+2):
        print(c,end=" ")
    print()






