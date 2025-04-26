import numpy as np
b1=[[1,2],[3,4]]
b2=[[5,6],[7,8]]
c=np.zeros((2,2),dtype=int)
for i in range(len(b1)):
    for j in range(len(b2)):
        c[i][j]=b1[i][j]+b2[i][j]
print(c)
