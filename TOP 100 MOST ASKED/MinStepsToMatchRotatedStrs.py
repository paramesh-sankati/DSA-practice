s1='abcde'
s2='cdeab'
def left_rotate(s1,s2):
    cnt=0
    for i in range(len(s1)-1):
        t=s1[i+1:]+s1[:i+1]
        cnt+=1
        if t==s2:
            break
    return cnt
def right_rotate(s1,s2):
    cnt=0
    for i in range(len(s1)-1,0,-1):
        t=s1[i:]+s1[:i]
        cnt+=1
        if t==s2:
            break
    return cnt
def minsteps(s1,s2):
    min_steps=min(left_rotate(s1,s2),right_rotate(s1,s2))
    return min_steps

print(minsteps(s1,s2))
