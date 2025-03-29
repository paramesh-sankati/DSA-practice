lst=[1,2,2,4,2,4,3,5,5,1,1,3,2,6,2,1,1]
dici={}
res=[]
max_cnt=0
for i in lst:
    if i not in dici:
        dici[i]=lst.count(i)
    if lst.count(i)>max_cnt:
        max_cnt=lst.count(i)
for k,v in dici.items():
   if v==max_cnt:
       res.append(k)
print(res)
       
