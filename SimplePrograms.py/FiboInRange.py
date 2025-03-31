#Fibonacci series upto a given number range
a=0
b=1
c=a+b
while a<=20:
    if c in range(10,20):
        print(c)
    c=a+b
    a=b
    b=c
