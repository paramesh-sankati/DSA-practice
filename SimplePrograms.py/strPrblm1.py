#first non repeating charecter

def getch(s):
    for i in s:
        if s.count(i)==1:
            return i
    return None


res=getch("abcab")

print(res)



