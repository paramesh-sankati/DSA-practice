n=5
asc2=64
for i in range(1,n+1):
    asc=65
    for j in range(1,n+1):
        if i+j>n:
            print(chr(asc),end=" ")
            asc+=1
        else:
            print(" ",end=" ")
    c=asc2
    for j in range(2,i+1):
        print(chr(c),end=" ")
        c-=1
    asc2+=1
    print()