'''colors=[1,8,3,8,3]
k=colors[0]
maxDis=0
for i in range(1,len(colors)):
    if colors[i]!=k:
        maxDis=max(maxDis,i-colors.index(k))
        k=colors[i]
print(maxDis)'''

