lst=[11,12,3,4,5,6]
k=4
max_sum=0
res=[]
for i in range(len(lst)):
    if i+k<=len(lst):
        if sum(lst[i:k+i])>max_sum:
            max_sum=sum(lst[i:k+i])
            res=lst[i:k+i]
    else:
        if sum(lst[i:]+lst[:(k+i)-len(lst)])>max_sum:
            max_sum=sum(lst[i:]+lst[:(k+i)-len(lst)])
            res=lst[i:]+lst[:(k+i)-len(lst)]

print(max_sum)
print(res) 

        