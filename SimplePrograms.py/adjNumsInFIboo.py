n=22
a=0
b=1
while True:
    s=a+b
    if n==b:
        print(a,s)
        break
    if n in range(b,s):
        print(b,s)
        break
    a=b
    b=s
    


    