# Project Euler #7 | Sidharth Baskaran | 01/08/2022

import time
import math

def is_prime(n):
    for x in range(math.ceil(math.sqrt(n)),1,-1):
        if n % x == 0:
            return False
    return True

def solve(count=10001):
    curr = 0
    p = 0
    idx = 0
    while curr <= count:
        p = 2*idx + 1
        if is_prime(p):
            curr += 1
        idx += 1
    print(p)


if __name__ == "__main__":
    s = time.time()
    solve()
    e = time.time()

    print('%.3fms' % ((e-s)*1000))