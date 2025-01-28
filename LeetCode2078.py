'''There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.'''
#brutalforce approach--log(N^2)
colors=[1,8,3,8,3]
high=0
for i in range(len(colors)):
    for j in range(i+1,len(colors)):
        if colors[i]!=colors[j]:
            high=max(high,(j-i))
print(high)