r=9
r1=(r+1)//2
c=10
for i in range(1,r1+1):
    for j in range(1,c+1):
        if j<=c//2:
            if i+j<=2*i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if i+j>c:
                print("*",end=" ")
            else:
                print(" ",end=" ")

    print()
for i in range(1,(r-r1)+1):
    for j in range(1,c+1):
        if j<=c//2:
            if i+j-1<c//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if j<=(c//2)+i:
                print(" ",end=" ")
            else:
                print("*",end=" ")
    print()