def peakElements(lst):
    peak_elements=[]
    for i in range(1,len(lst)-1):
        if lst[i]>lst[i-1] and lst[i]>lst[i+1]:
            peak_elements.append(lst[i])
    return peak_elements
        


lst=[1,2,3,4,8,7,9,6]
print(peakElements(lst))