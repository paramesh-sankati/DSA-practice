'''
Sum of digits powered by their position is equal to the number.
(e.g., 135 → 1¹ + 3² + 5³ = 135)
'''

n=135
s1=str(n)
s=0
for i in range(len(s1)):
    s=s+(int(s1[i])**(i+1))
print(s)