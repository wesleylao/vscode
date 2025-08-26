import math, itertools
l = ['a', 'b', 'c']
#print(list(itertools.permutations(l)))
n = len(l)
i = 0
j = 0
tmp = 0
for j in range(n):
    for i in range(j, n):
        l[i], l[j] = l[j], l[i]
        print(l)
        tmp += 1
        l[i], l[j] = l[j], l[i] 

print(tmp, '種組合')