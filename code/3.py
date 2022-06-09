# Project Euler #1 | Sidharth Baskaran | 02/14/2022

import time
import math

def is_prime(k):
    if k == 1:
        return False
    i = 2
    while i ** 2 <= k:
        if k % i == 0:
            return False
        i += 1
    return True

def solve(n):
    if is_prime(n):
        return n
    # then largest factor has to be <= sqrt(n)
    for i in range(math.ceil(math.sqrt(n)), 2, -2):
        if is_prime(i) and n % i == 0:
            return i
    
if __name__ == "__main__":
    s = time.time()
    print(solve(600851475143))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))