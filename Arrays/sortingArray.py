arr=[34,2,35,1,6,3,2,56]
n=len(arr)
for i in range(n):  #each time one is compared with all other and swapped if greater
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]  #swapping
print(arr)
