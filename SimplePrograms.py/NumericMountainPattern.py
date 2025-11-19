n=int(input("Enter number of rows:"))
c=1
u=(n+1)//2
for i in range(1,u+1):
    for j in range(i):
        print(c,end=" ")
        c+=1
    print()
c-=2
l=(n-1)//2
for i in range(l,0,-1):
    for j in range(i):
        print(c,end=" ")
        c-=1
    print()


