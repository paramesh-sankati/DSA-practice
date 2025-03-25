n=4
a=0
b=1
fib=[]
for i in range(n*(n+1)//2):
    c=a+b
    fib.append(c)
    a=b
    b=c
c=0
for i in range(1,n+1):
    for j in range(i):
        print(fib[c],end=" ")
        c+=1
    print()
