def isset(a,k):
    if a&(1<<k)==0:
        return True
    else:
        return False
    
a=10
k=2
print(isset(a,k))