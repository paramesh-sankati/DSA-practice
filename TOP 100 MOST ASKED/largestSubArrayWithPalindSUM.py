def largest(n,lst):
    if n<5:
        return "Invalid Array size"
    max_len=float('-inf')
    ans=[]
    for i in range(n):
        for j in range(i+1,n+1):
            c=str(sum(lst[i:j]))
            if len(lst[i:j])>=2 and c==c[::-1]:
                if len(lst[i:j])>max_len:
                    max_len=len(lst[i:j])
                    ans=lst[i:j]
    else:
        if len(ans)==0:
            ans='No Sub Arrays Found'
    return ans
n=5
lst=[10,20,30,6,19]
print(largest(n,lst))
