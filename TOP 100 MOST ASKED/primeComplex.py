n=8
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
def primeRange(n):
    cnt=0
    i=2
    arr=[]
    while True:
        if isPrime(i):
            arr.append(i)
            cnt+=1
        if cnt==n:
            return arr
        i+=1
def required(m):
    n=abs(m)
    prime_numbers=primeRange((n*(n+1))//2)
    ind,start=-1,0
    while ind<=((n*(n+1))//2)-2:
        for i in range(start):
            ind+=1
        else:
            ind+=1
            if m<0:
                print(prime_numbers[ind]*-1,end=" ")
            else:
                print(prime_numbers[ind],end=" ")
        start+=1
        
required(n)
        
    
