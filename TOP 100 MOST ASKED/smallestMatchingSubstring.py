s="adobecodebanc"
t='abc'
res=''
min_length=float('inf')
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if len(s[i:j])<min_length and set(t).intersection(set(s[i:j]))==set(t):
            res=s[i:j]
            min_length=len(s[i:j])
print(res,min_length)

