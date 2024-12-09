# L1 = L2 = [2]
# print(L1 is L2)

# x = int(input())
# if x % 2 == 0:
#     # pass
#     print(x, "is even")
# else:
#     print(x, "is odd")

# x = int(input("which age so you like: "))
# print("FBI open up!!!") if x <= 14 else print("bruh")

# t = input()
# print("%s is a palindrome. " %t) if t == t else print("%s is not a palindrome." %t)

# n = int(input())
# i = 1
# j = 1
# while n > 0:
#     i = i * n
#     j = j * (n-1)
#     n = n - 2     
# print(i, j)

# L = []
# n = 0 
# while n < 10:
#     L = L + [n]
#     n = n + 1
# print(len(L), L)

# row, column = 30, 4
# r = 0
# while r < row:
#     c = 0
#     L = []
#     while c < column:
#         L = L + [r + c]
#         c = c + 1
#     print(L)
#     r = r + 10

# x = int(input())
# y = int(input())
# r = "o"
# while x != 0:
#     s = ""
#     tmp = y
#     while tmp != 0:
#         s += r
#         r = "x" if r == "o" else "o"  
#         tmp = tmp - 1
#     r = "x" if s[0] == "o" else "o"
#     print(s)    
#     x = x - 1

# n = int(input())
# k = 2
# l = []
# while k < n:
#     if n % k == 0:
#         l += [k]
#     k += 1
# if l == [] :
#     print(n,'is a prime number')
# else:
#     l += [n]
#     print(n, l) 

# def eratosthenes(n):
#     is_prime = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n + 1, i):
#                 is_prime[j] = False
#     return [x for x in range(2, n + 1) if is_prime[x]]
# print(eratosthenes(120))

A = [10, 5, 1, 6, 9, 2, 6, 9, 10, 8]
a = sorted(A)
aa = int(len(a))
min_A, max_A = int(a[0]), int(a[-1])
if aa % 2 != 0: 
    median_A = a[aa//2]  
else:
    median_A = (a[aa//2] + a[aa//2-1])/2
print(min_A, max_A, median_A)
mean_A = sum(a)//aa
ia = 0
tmp = 0
std = 0
while ia < aa:
    tmp = (a[ia]-mean_A)**2
    std += tmp
    ia += 1
sdm = (std/(aa-1))**0.5
print(sdm)    