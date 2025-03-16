n=5
c=1
for i in range(n):
    for j in range(n-i):
        if c<10:
            print(" ",end="")
        print(c,end=" ")
        c=c+1
    print()