'''
Given an array list of non-negative integers, return the maximum product of two numbers possible.
Input: arr[] = [1, 4, 3, 6, 7, 0] 
Output: 42
Explanation: 6 and 7 have the maximum product.

'''
def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

lst=[1, 4, 3, 6, 7, 0]
print(max_product(lst))