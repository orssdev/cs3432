from math import sqrt

prime_nums = [2,3,5,7]

for i in range(11,10**9 + 1):
    sqrt_floor_i = int(sqrt(i))
    isPrime = True
    for p in [prime for prime in prime_nums if prime < sqrt_floor_i]:
        if i % p == 0:
            isPrime = False
    if isPrime:
        prime_nums.append(i)
        print(i)
