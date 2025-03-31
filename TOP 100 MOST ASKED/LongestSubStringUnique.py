s="alexander"
max_length=0
sub=''
for i in range(len(s)):
    for j in range(i,len(s)):
        lst=[]
        for k in range(i,j+1):
            lst.append(s[k])
            if len(lst)==len(set(lst)):
                if len(lst)>max_length:
                    max_length=len(lst)
                    sub="".join(lst)               
print(max_length)
print(sub)
