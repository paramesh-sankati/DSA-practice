lst=[-2,1,-3,4,-1,2,1,-5,4]
max_sum=float('-inf')
q=""
for i in range(len(lst)):
    for j in range(i,len(lst)):
        s=0
        s1=""
        for k in range(i,j+1):
            s=s+lst[k]
            s1=s1+str(lst[k])+" "
            if s>max_sum:
                max_sum=s
                q=s1

print(max_sum)
print(q)
