# Project Euler #21 | Sidharth Baskaran | 04/02/2022

import time
from functools import reduce
from itertools import combinations

# sum of proper divisors of n
def d(n):
    # generate a list of primes
    A = [True] * (n + 1)
    i = 2
    while i ** 2 <= n:
        if A[i]:
            for j in range(i ** 2, n + 1, i):
                A[j] = False
        i += 1
    primes = [i for i in range(2, n//2 + 1) if A[i]]
    # generate prime factorization
    factorization = []
    for p in primes:
        c = n
        while c % p == 0:
            factorization.append(p)
            c //= p
    # generate list of divisors
    divisors = [1]
    for k in range(1, len(factorization) + 1):
        for comb in combinations(factorization, k):
            prod = reduce(lambda x,y: x * y, comb)
            if prod < n:
                divisors.append(prod)
    divisors = list(set(divisors))
    return sum(divisors)

def solve_brute():
    amicable = []
    for i in range(10000):
        if d(i) < 10000 and i != d(i) and i == d(d(i)):
            amicable.append(i)
            amicable.append(d(i))
    return sum(set(amicable)) # set to prevent double counting

if __name__ == "__main__":
    s = time.time()
    print(solve_brute())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))