arr1=[5,8,3,2,7,3]
arr2=[1,2,2,3,3,3,4,4,4,4]
res=[]
for i in arr1:
    if i not in res:
        if i in arr2:
            for j in range(min(arr1.count(i),arr2.count(i))):
                res.append(i)
print(res)



