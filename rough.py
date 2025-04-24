# Online Python compiler (interpreter) to run Python online.
ratios={}
N,W=3,20
profits=[25,24,15]
weights=[18,15,10]
for i in range(N):
    ratios[(profits[i],weights[i])]=round(profits[i]/weights[i],2)
sorted_ratios=dict(sorted(ratios.items(),key=lambda item:item[1],reverse=True))
inserted_weight,max_profit=0,0
wts_after_sorting=[]
pfts_after_sorting=[]
for i in sorted_ratios.keys():
    wts_after_sorting.append(i[1])
for i in sorted_ratios.values():
    pfts_after_sorting.append(i)
i=0
while inserted_weight<W:
    remaining_weight=W-inserted_weight
    if wts_after_sorting[i]<=remaining_weight:
        max_profit=max_profit+wts_after_sorting[i]*pfts_after_sorting[i]
        inserted_weight=wts_after_sorting[i]
        i+=1
    else:
        max_profit=max_profit+(remaining_weight-wts_after_sorting[i])*pfts_after_sorting[i]
        break
print(max_profit)
