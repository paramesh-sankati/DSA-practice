org='Pro            gram'
fs=org.index(' ')
ls=org.rindex(' ')
print(fs,ls)
c=fs
while fs<=ls+1:
    s=org[:c]+org[fs:]
    print(s)
    fs+=1

