'''
3.	Find the Majority Element (Moore’s Voting Algorithm)
Given an array of size n, find the majority element (an element that appears more than n/2 times).
Example:
Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
Output: 4
'''

lst=[3, 3, 4, 2, 4, 4, 2, 4, 4]
dici={}
for i in lst:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
for k,v in dici.items():
    if v>len(lst)//2:
        print(k)