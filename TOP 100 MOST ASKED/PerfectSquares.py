n=12
i=1
arr=[]
while i**2<=n:
    arr.append(i**2)
    i+=1
min_cnt=0
cnt=0
for i in range(len(arr)):
    if arr[i]==n:
        min_cnt+=1
        break
    if n%arr[i]==0:
        min_cnt=n//arr[i]
    if arr[i]<n:
        





