arr=[1,2,3,2,23,13,232,323,33]
key=int(input("Enter number to be searched: "))

#using in operator 
if key in arr:
    print(arr.index(key))
else:
    print("Element doesn't exist")

#using loop
for i in range(len(arr)):
    if arr[i]==key:
        print(i)
else:
    print("Element doesn't exist")