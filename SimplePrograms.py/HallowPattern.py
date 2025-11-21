n=int(input("Enter n:"))

for i in range(1,n+1):
    print(n*' '+(n-i)*' '+i*'* ')

for i in range(1,n+1):
    print((n-i)*' '+i*'* '+(n-i)*'  '+i*'* ')


