#Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
#Return the maximum difference. If no such i and j exists, return -1.
#optimal way
def MaxDifference(li:list[int]):
    least=li[0]
    ans=-1
    for i in range(1,len(li)):
        if least<li[i]:
            ans=max(ans,li[i]-least)
        least=min(least,li[i])
    return ans
nums=[5,4,6,3]
res=MaxDifference(nums)
print(res)