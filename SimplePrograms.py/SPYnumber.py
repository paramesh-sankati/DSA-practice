'''
Spy Number

Sum and product of digits are equal.
(e.g., 123 → 1+2+3 = 6, 1×2×3 = 6)'''

n=123
s=0
m=1
while n>0:
    r=n%10
    s=s+r
    m=m*r
    n=n//10
if s==m:
    print("SPY Number")
else:
    print("Not a SPY Number")