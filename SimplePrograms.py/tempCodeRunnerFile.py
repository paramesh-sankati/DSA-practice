#reverse each word of a given string
s="reverse each word of a given string"
s1=""
for i in s.split():
    s1=s1+i[::-1]+" "
print(s1)