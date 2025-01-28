r=5
for i in range(r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    for j in range(i):
        print(j+2,end=" ")
    print()