'''
Given an array of numbers, return an array such that each element at index i is the product of all the numbers in the original array except the one at index i.
Example:
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
'''
lst=[1,2,3,4]
res=[]
for i in range(len(lst)):
    m=1
    for j in range(len(lst)):
        if j==i:
            continue
        else:
            m=m*lst[j]
    res.append(m)
print(res)



        