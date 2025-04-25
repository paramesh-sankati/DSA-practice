def case_conversion(s):
    if ord(s)>=97:
        return chr(ord(s)-32)
    else:
        return chr(ord(s)+32)

l='p'
print(case_conversion(l))
