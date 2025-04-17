n=52
s=''
while n>26:
    if n%26==0:
        s=chr(90)+s 
        print(s)   
    else:
        s=chr((n%26)+64)+s
    n=n//26
else:
    print(n)
    s=chr(n+64)+s
    print(chr(n+64))
print(s)
