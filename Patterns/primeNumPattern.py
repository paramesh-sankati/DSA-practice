n=4
pri=[2,3]
for i in range(1,n*(n+1)):
    for j in range(2,i//2+1):
        if i%j==0:
            break
        else:
            pri.append(i)
            break
c=0
for i in range(1,n+1):
    for j in range(i):
        print(pri[c],end=" ")
        c+=1
    print()
    

