A = [10, 5, 1, 6, 9, 2, 6, 9, 10, 8]
B = [13, 9, 1, 8, 10, 7, 3, 4, 18, 2]
C = [86, 10, 26, 66, 97, 35, 69, 31, 89, 67]

################################

#TODO
a = sorted(A)
aa = int(len(a))
min_A, max_A = int(a[0]), int(a[-1])
if aa % 2 != 0: 
    median_A = a[aa//2]  
else:
    median_A = (a[aa//2] + a[aa//2-1])/2

b = sorted(B)
bb = int(len(b))
min_B, max_B = int(b[0]), int(b[-1])
if bb % 2 != 0: 
    median_B = b[bb//2]  
else:
    median_B = (b[bb//2] + b[bb//2-1])/2

c = sorted(C)
cc = int(len(c))
min_C, max_C = int(c[0]), int(c[-1])
if cc % 2 != 0: 
    median_C = c[cc//2]  
else:
    median_C = (c[cc//2] + c[cc//2-1])/2

################################

print(max_A, min_A, median_A)
print(max_B, min_B, median_B)
print(max_C, min_C, median_C)

################################

#TODO
mean_A = sum(a)/aa
ia = 0
tmpA = 0
stdA = 0
while ia < aa:
    tmpA = (a[ia]-mean_A)**2
    stdA += tmpA
    ia += 1
sdm_A = (stdA/(aa-1))**0.5

mean_B = sum(b)/bb
ib = 0
tmpB = 0
stdB = 0
while ib < bb:
    tmpB= (b[ib]-mean_B)**2
    stdB += tmpB
    ib += 1
sdm_B = (stdB/(bb-1))**0.5

mean_C = sum(c)/cc
ic = 0
tmpC = 0
stdC = 0
while ic < cc:
    tmpC = (c[ic]-mean_C)**2
    stdC += tmpC
    ic += 1
sdm_C = (stdC/(cc-1))**0.5

################################

print(sdm_A)
print(sdm_B)
print(sdm_C)