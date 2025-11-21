n=int(input('Enter rows n= '))
s=int(input('enter start s='))
for i in range(1,n+1):
    print(i*str(s))
    s+=1
s-=2
for i in range(n-1,0,-1):
    print(i*str(s))
    s-=1
