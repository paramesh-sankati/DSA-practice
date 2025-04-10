list1=[23,8,91,-9,0,23,-2]
def minmax(arr,low,high):
    if low==high:
        return list1[low],list1[high]
    elif high==low+1:
        if list1[low]>list1[high]:
            return list1[high],list1[low]
        else:
            return list1[low],list1[high]
    else:
        mid=(low+high)//2
        min1,max1=minmax(low,mid)
        min2,max2=minmax(mid+1,high)
        org_min=minimum()