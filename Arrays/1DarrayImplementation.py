num=int(input("how many elements to store inside the array: "))
arr=[]
for i in range(num):
    element=int(input("Enter {} element into array:".format(i+1)))
    arr.append(element)
print(arr)
