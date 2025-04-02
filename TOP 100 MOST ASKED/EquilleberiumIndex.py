#Equilleberium Index
arr=[1,2,6,4,5,4]
for i in range(1,len(arr)-1):
    ls=sum(arr[:i])
    rs=sum(arr[i+1:])
    if ls==rs:
        print(i)
        



