import math, itertools
l = ['a', 'b', 'c', 'd']
#print(list(itertools.permutations(l)))
n = len(l)  
i = 0
j = 0
for j in range(n):
    for i in range(j, n):
        l[i], l[j] = l[j], l[i]
        print(l)
        l[i], l[j] = l[j], l[i] 

print(math.factorial(n), '種組合')