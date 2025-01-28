r=5
c=5
for i in range(r):
    for j in range(c-i):
        print(" ",end=" ")
    for k in range(c):
        print("*",end=" ")
    if j!=c-1:
        print(" ",end="")
    print()