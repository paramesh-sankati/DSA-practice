n=int(input('Enter n:'))
for i in range(1,n+1):
    c=1
    for j in range(i):
        print(i*c,end=" ")
        c+=1
    print()
k=n-1
for i in range(n+1,2*n):
    c=1
    for j in range(k,0,-1):
        print(i*c,end=" ")
        c+=1
    k-=1
    print()