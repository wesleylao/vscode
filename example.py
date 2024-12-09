L = [100, 97, 13, 100, 56, 97, 17, 32, 97, 56]
P = []
NP = []
for n in L:
    k = 2
    while k < n:
        if n % k == 0:
            break
        k += 1
    if k == n:        
        P += [n]
    else:
        NP += [n]
print('Prime numbers:', P)
print('Non-prime numbers:', NP)
