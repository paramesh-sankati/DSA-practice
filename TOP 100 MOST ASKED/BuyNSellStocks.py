lst=[100, 180, 260, 310, 40, 535, 695]
i=0
j=1
max_profit=0
while j<len(lst):
    if lst[j]-lst[i]>max_profit:
        max_profit=lst[j]-lst[i]
    if lst[j]<lst[i]:
        i=j
    j+=1
print(max_profit)
