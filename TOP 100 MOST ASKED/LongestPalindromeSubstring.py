s='babad'
mul_pal=[]
long_sub=0
for i in range(len(s)):
    for j in range(i,len(s)):
        t=s[i:j+1]
        if t==t[::-1]:
            if len(t)>long_sub:
                ans=t
                long_sub=len(t)
print(ans)



    
    
    