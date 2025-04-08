arr=[[1,3,2],[12,34,23],[32,2,65]]
rowMax=float('-inf')
max_ind=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]>rowMax:
            rowMax=arr[i][j]
            max_ind=j
    print("Row-{} Max num is {} at {} index".format(i+1,rowMax,max_ind))

