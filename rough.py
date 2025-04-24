'''
Given weights and values of N items, we need to put these items in a knapsack of capacity
W to get the maximum total value in the knapsack.
Note: you are allowed to break the item.
Approach we required to get maximum profit.
N=3 and W=20
Profits=[25,24,15]
Weights=[18,15,10]
Max profit=31.5 around

'''
N,W=3,20
profits=[25,24,15]
weights=[18,15,10]
def max_profit_greedy(N,W,p,wts):
    ratios={}
    for i in range(N):
        ratios[weights[i]]=round(profits[i]/weights[i],2)
    sorted_ratios=dict(sorted(ratios.items(),key=lambda item:item[1],reverse=True))
    print(sorted_ratios)
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
            max_profit=max_profit+(abs(remaining_weight-wts_after_sorting[i]))*pfts_after_sorting[i]
            break
    return max_profit
print(max_profit_greedy(N,W,profits,weights))
