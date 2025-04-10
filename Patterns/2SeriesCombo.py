r=6
total=(r*(r+1))//2
if total%2==0:
    en=fn=total//2
else:
    en=total//2
    fn=(total//2)+1
even=[]
cnt=0
n=1
while cnt<en:
    if n%2==0:
        even.append(n)
        cnt+=1
    n+=1
a=1
b=1
fibo=[a,b]
while len(fibo)<fn:
    s=a+b
    fibo.append(s)
    a=b
    b=s
c=1
ei=fi=0
for i in range(1,r+1):
    for j in range(i):
        if c%2!=0:
            print(fibo[fi],end=" ")
            fi+=1
        else:
            print(even[ei],end=" ")
            ei+=1
        c+=1
    print()
    


