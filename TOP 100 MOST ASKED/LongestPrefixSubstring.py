strs = ["aaa","aa","aaa"]
ans=""
temp=''
for i in strs[0]:
    temp+=i
    for j in range(len(strs)):
        if strs[j].startswith(temp):
            if j==len(strs)-1:
                ans=temp
        else:
            break
print(ans)