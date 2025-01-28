def maxProfit(prices) -> int:
    leastPrice=min(prices)
    i=prices.index(leastPrice)
    print(i)
    if len(prices[i+1:])==0:
        return 0
    else:
        profit=max(prices[i+1:])-leastPrice
        print(profit)
        print(leastPrice)
        if profit!=leastPrice:
            return profit
        else:
            return 0
prices=[1,2]
res=maxProfit(prices)
print(res)
print(max([2]))