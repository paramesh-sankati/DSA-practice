'''10.	Find the Kth Largest Element
Given an integer array, find the kth largest element.
Example:
Input: [3, 2, 1, 5, 6, 4], k = 2
Output: 5
'''
lst=[3, 2, 1, 5, 6, 4]
k=int(input("enter number: "))
lst1=list(set(lst))
lst1.sort(reverse=True)
print(lst1[k-1])