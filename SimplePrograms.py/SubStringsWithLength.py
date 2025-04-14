s='abcdef'
k=3
for i in range(len(s)):
    for j in range(i,len(s)+1):
        if len(s[i:j])==k:
            print(s[i:j])
