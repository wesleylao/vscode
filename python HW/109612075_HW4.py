row = 3
col = 4 #Just for example
#TODO
################################

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers(m):
    primes = []
    num = 2
    while len(primes) < m:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def print_prime_2d_array(rows, columns):
    m = rows * columns
    primes = generate_prime_numbers(m)
    
    prime_2d_array = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(primes[index])
            index += 1
        prime_2d_array.append(row)
    
    for row in prime_2d_array:
        print(row)
a = print_prime_2d_array(row, col)
print(a)




################################
# [[2, 3, 5, 7],
# [11, 13, 17, 19],
# [23, 29, 31, 37]]
