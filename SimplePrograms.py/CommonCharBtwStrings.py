s1='abhiram'
s2='abhi'
res=set()
for i in s1:
    if i in s2:
        res.add(i)
print(list(res))
