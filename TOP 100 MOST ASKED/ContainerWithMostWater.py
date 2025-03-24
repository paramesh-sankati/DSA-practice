'''
Given an array where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that holds the most water.
Example: 
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''
lst=[1,8,6,2,5,4,8,3,7]
h=0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        k=(j-i)*min(lst[i],lst[j])
        if k>h:
            h=k
print(h)
