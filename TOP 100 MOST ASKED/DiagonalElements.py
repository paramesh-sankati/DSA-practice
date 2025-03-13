lst=[[1,2,3],[4,5,6],[7,8,9]]
n=len(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        """ if i==j:
            print(lst[i][j]) """
        if i+j==n-1:
            print(lst[i][j])
