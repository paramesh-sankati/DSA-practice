s='AZ'
if len(s)==1:
    print(ord(s[0])-64)
else:
    c=0
    ans=0
    for i in range(len(s)-1,-1,-1):
        ans=ans+(ord(s[c])-64)*(26**i)
        c+=1
print(ans)