def highest_on_right(arr):
    ans=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j]>lst[i]:
                ans.append(lst[j])
                break
        else:
            ans.append(-1)
    return ans


lst=[24,3,5,2,55,2,0,-4,-2,54,34,-45,3]
print(highest_on_right(lst))