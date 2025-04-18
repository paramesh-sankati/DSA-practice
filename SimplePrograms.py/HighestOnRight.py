def highest(lst,k):
    i=lst.index(k)
    for j in range(i+1,len(lst)):
        if lst[j]>k:
            return lst[j]
    else:
        return -1

lst=[24,-12,3,23,-3,4,-56,7,43,67]
k=24
print(highest(lst,k))
