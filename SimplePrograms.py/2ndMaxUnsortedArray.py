arr=[23,1,34,67,54,46,6,45]
first_max=float('-inf')
sec_max=float('-inf')
for i in arr:
    if i>first_max:
        first_max=i
for i in arr:
    if i>sec_max and i!=first_max:
        sec_max=i
print(sec_max)