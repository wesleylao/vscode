L = [10, 20, 30, 'ABC', '123', '456']
#L = [10, 20, 30, 'ABC', '123', '456', 'XYZ']

################################
#TODO

n = len(L)
if n % 2 == 0:
    L = L[n // 2::1] + L[:n//2]
else:
    L = L[n//2+1::1] + L[:n//2+1] 

#TODO


################################

print(L)