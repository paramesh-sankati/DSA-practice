'''
Q1:Write a function to mask email address
Input:mayurkulkarni636@gmail.com
Output:m###############@gmail.com

'''
s='parameshyadav865@gmail.com'
ans=s[0]
i=1
while s[i]!='@':
    ans+='#'
    i+=1
else:
    ans+=s[i:]
print(ans)

