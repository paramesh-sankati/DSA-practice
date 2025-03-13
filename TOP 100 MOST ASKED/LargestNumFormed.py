'''
12.	Largest Number Formed from an Array
Given a list of non-negative integers, arrange them in such a way that they form the largest number.
Example:
Input: [3, 30, 34, 5, 9]
Output: 9534330
'''
lst=[3, 30, 34, 5, 9]
res=[str(i).split() for i in lst]
print(res)