n=int(input('Enter n :'))

for i in range(n-1,0,-1):
    print(((n-1)-i)*' '+'* '+(i-1)*'  '+'*')