# m, n = 6, 3 #Just for example
m, n = 7, 3
#TODO
################################
L = []
k = 0
tmp = [i for i in range(0, n*m, )]
while k < m*n:
    L += [tmp[k: k+n: ]] + [tmp[k+2*n-1: k+n-1: -1]]
    k += 2*n
if m % 2 != 0:
    L.pop()
################################
print(L) #[[0, 1, 2],[5, 4, 3],[6, 7, 8],[11, 10, 9],[12, 13, 14],[17, 16, 15]]