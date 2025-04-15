s='My age is 23 and my brother is 30'
for i in s.split():
    s=0 
    for j in i:
        if j.isdigit():
            s+=int(j)
    print(i,s)
