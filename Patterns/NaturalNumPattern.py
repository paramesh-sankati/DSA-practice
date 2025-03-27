n=5
lst=[0]
temp=list(range(n-1,0,-1))
lst.extend(temp)
c=1
for i in range(1,n+1):
    m=c
    for j in range(i):
        m=m+lst[j]
        print(m,end=" ")
    c+=1
    print()

