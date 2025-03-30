# program to Reverse Number 
n=1234
print(int(str(n)[::-1]))

#program to calculate the sum of digits of a number
s=0
for i in str(n):
    s+=int(i)
print(s)

#reverse each word of a given string
s="reverse each word of a given string"
s1=""
for i in s.split():
    s1=s1+i[::-1]+" "
print(s1)