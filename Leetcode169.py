#Majority Element
#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
def majorityElement(nums) -> int:
    n=len(nums)
    dic={}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    ans=-1
    for i in dic:
        val=dic[i]
        if val>n/2:
            ans=i
            break
    return ans

nums=[2,2,1,1,1,2,2]
res=majorityElement(nums)
print(res)


#another way but more tym complexity
lis=[1,2,1,2,1,2,1,2,1,1]  
n=len(lis)    #in qn req element should be  greater than n/2 
#means if we sort it will be middle element
lis.sort()
print(lis[n//2])
