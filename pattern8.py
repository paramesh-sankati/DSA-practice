r=5
for i in range(r):
    for j in range(i):
        print(" ",end=" ")
    for k in range((r*2-1)-(i*2)):
        print("*",end=" ")
    print()
