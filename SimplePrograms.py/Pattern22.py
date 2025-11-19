n=int(input("Enter rows :"))
c=1
for i in range(1,n+1):
    s=n*i
    c=s+1-n
    for j in range(n):
        if i%2==0:
            print(s,end=" ")
            s-=1
        else:
            print(c,end=" ")
            c+=1
    print()
        
            
        