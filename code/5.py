# Project Euler #5 | Sidharth Baskaran | 02/15/2022

import time
from collections import Counter

def is_prime(k):
    if k == 1:
        return False
    i = 2
    while i ** 2 <= k:
        if k % i == 0:
            return False
        i += 1
    return True

def get_pf(n):
    prime_factors = {}
    # express n = p1^f1 + p2^f2 + ... + pn^fn
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            nc = n
            c = 0
            while nc % i == 0:
                c += 1
                nc /= i
            prime_factors[i] = c
    return Counter(prime_factors)

# strategy = check the number's prime factorization
def solve():
    # get prime factors of all in range(1,21)
    check_factors = Counter()
    for i in range(2,21):
        for c in get_pf(i):
            check_factors[c] = max(check_factors[c], get_pf(i)[c])
    print(check_factors)
    
    # get the result
    res = 1
    for c in check_factors:
        res *= c**check_factors[c]
    print(res)
            
if __name__ == "__main__":
    s = time.time()
    solve()
    e = time.time()
    print('%.3fms' % ((e-s)*1000))