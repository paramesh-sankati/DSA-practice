li=[1,5,8,0,1,8,1,5,1]
dic={}
for i in li:
    if i in dic:   #O(1) time complexity in dic but O(N) in list
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
for k,v in dic.items():
    print("{}-->{}".format(k,v))