'''
13.	Move Zeroes to the End
Given an array of integers, move all the zeroes to the end while maintaining the relative order of the non-zero elements.
Example:
Input: [0, 1, 2, 0, 3, 4]
Output: [1, 2, 3, 4, 0, 0]

'''
lst=[0, 1, 8,9,4,2,0, 3, 4]
res=[]
zeros=[]
for i in lst:
    if i==0:
        zeros.append(i)
    else:
        res.append(i)
res.extend(zeros)
print(res)
