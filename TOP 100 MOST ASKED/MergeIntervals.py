'''
7.	Merge Intervals
Given a collection of intervals, merge all overlapping intervals.
Example:
Input: [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
'''
res=[]
lst=[[1,3],[2,6],[8,10],[15,18]]
for i in range(len(lst)-1):
    if lst[i][1]>=lst[i+1][0]:
        res.append([lst[i][0],lst[i+1][1]])
    else:
        res.append(lst[i])
    
print(res)


