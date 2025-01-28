#Given an array of integers nums, return the number of good pairs.

#A pair (i, j) is called good if nums[i] == nums[j] and i < j.
def numIdenticalPairs(nums) -> int:
    ans=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                ans+=1
    return ans

l=[1,2,3,1,1,3]
res=numIdenticalPairs(l)
print(res)


#optimal way---sum of n natural nmbrs
def numIdenticalPairs2(nums) -> int:
        dics={}
        for i in nums:
            if i in dics:
                dics[i]+=1
            else:
                dics[i]=1
        ans=0
        for i in dics:
            n=dics[i]
            temp=n*(n-1)/2
            ans=ans+temp
        return int(ans)

res1=numIdenticalPairs2(l)