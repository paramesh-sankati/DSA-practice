n=5
t=1
for i in range(n,0,-1):
    temp=t
    c=i
    for j in range(n-i+1):
        if i+j==n:
            print(j+1,end=" ")
        else:
            print(temp,end=" ")
            temp=temp-c
        c=c+1
    t+=i
    print()
