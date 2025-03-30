#program to Count Vowels and Consonants in a given string
s="aeiou"
vc=0
cc=0
for i in s:
    if i in {'a','e','i','o','u'}:
        vc+=1
    else:
        cc+=1
print("vowel count={} consonant count={}".format(vc,cc))
