lst=[[1,2,3],[4,5,6],[7,8,9]]
n=len(lst)
s=0
for i in range(len(lst)):
    #print(lst[i][n-1-i])
    #print(lst[i][i])
    s=s+lst[i][n-1-i]+lst[i][i]
print(s)
