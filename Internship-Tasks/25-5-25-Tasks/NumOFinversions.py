def num_of_inversions(lst):
    cnt,j=0,1
    for i in range(len(lst)-1):
        if lst[i]>lst[j]:
            cnt+=1
        j+=1
    return cnt
arr=[1,3,5,6,7]
arr=[2,7,3,4,11,9,21,6,1]
print(num_of_inversions(arr))