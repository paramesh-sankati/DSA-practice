k=63
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
i=4
a=2
b=3
while True:
    if k==1:
        print(a)
        break
    if k==2:
        print(b)
        break
    if isprime(i):
        if b==k:
            if b-a<i-a:
                print(a)
                break
            elif b-a>i-a:
                print(i)
                break
            else:
                print(a,i)
                break
    
        if k in range(b,i):
            if k-b<i-k:
                print(b)
                break
            elif k-b>i-k:
                print(i)
                break
            else:
                print(b,i)
                break
        a=b
        b=i
    i+=1






