s1='20022000'
s2='09092005'
def isEligible(arr):
    print(int(s1[4:]))
    print(int(''.join(str(i) for i in arr[4:])))
    if int(''.join(str(i) for i in arr[4:]))>=int(s1[4:]) and int(''.join(str(i) for i in arr[4:]))<=int(s2[4:]):
        if int(''.join(str(i) for i in arr[2:4]))>=int(s1[2:4]) and int(''.join(str(i) for i in arr[2:4]))<=int(s2[2:4]):
            if int(''.join(str(i) for i in arr[:2]))>=int(s1[:2]) and int(''.join(str(i) for i in arr[:2]))<=int(s2[:2]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
#Error

print(isEligible([1,9,0,7,2,0,0,3]))



