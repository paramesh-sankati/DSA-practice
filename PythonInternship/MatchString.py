def ismatch(s,p):
    for i in range(len(s)-len(p)+1):
        if s[i:len(p)+i]==p:
            return True
    else:
        return False

s="abababababababababcccbababbc"
p="abcccb"
print(ismatch(s,p))