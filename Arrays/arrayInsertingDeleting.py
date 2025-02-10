arr=[1,2,3,4,5,6,7]

#inserting 
arr.append(23)   #added at last
arr.insert(2,34)   #inserted at index 2

print(arr)

#deleting
arr.pop()  #removes last element
arr.pop(3)  #removes specified index element

ele=int(input("enter element to be removed :"))
if ele in arr:
    arr.remove(34)   #removes specified element
else:
    print("Element doesn't exist")

print(arr)