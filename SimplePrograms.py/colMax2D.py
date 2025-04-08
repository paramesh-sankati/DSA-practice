arr=[[1,3,2],[12,34,23],[32,2,65]]
r,c=3,3
colMax=float('-inf')
max_ind=0
for i in range(c):
    for j in range(r):
        if arr[j][i]>colMax:
            colMax=arr[j][i]
            max_ind=j
    print('col-{} max is {} at index-{}'.format(i,colMax,max_ind))
