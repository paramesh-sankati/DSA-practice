list1=[23,8,91,-9,0,23,-2]
def minmax(list1,low,high):
    if low==high:
        return list1[low],list1[high]
    elif high==low+1:
        if list1[low]>list1[high]:
            return list1[high],list1[low]
        else:
            return list1[low],list1[high]
    else:
        mid=(low+high)//2
        min1,max1=minmax(list1,low,mid)
        min2,max2=minmax(list1,mid+1,high)
        org_min=minimum(min1,min2)
        org_max=maximum(max1,max2)
    return org_min,org_max
def minimum(a,b):
    if a<b:
        return a
    else:
        return b
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
low=0
high=len(list1)-1
print(minmax(list1,low,high))


