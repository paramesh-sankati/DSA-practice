'''
Bheem has N friends and he has a ladoo for each day given an list denoting on which day i th index friend wants a ladoo if bheem is unable to give a ladoo to the friend he loses his friendship with them find out the maximum number of friends he can have at the end
Example: N=5
List of days=[3,3,1,2,4]
Output=4

'''
def max_friends(n,lst):
    cnt=0
    res={}
    for i in range(n):
        if lst[i] not in res:
            res[lst[i]]=1
            cnt+=1
    return cnt
N=5
days=[3,3,1,2,4]
print(max_friends(N,days))
         

