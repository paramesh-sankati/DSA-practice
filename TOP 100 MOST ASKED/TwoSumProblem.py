'''
4.	Two Sum Problem
Given an array of integers and a target number, return the indices of the two numbers such that their sum is equal to the target.
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

'''
lst=[2,7,11,15]
t=9
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==t:
            print([i,j])
