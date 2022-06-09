# Project Euler #10 | Sidharth Baskaran | 03/18/2022

import time

def solve(n):
    # generate a sieve
    A = [True] * (n + 1)
    i = 2
    while i ** 2 <= n:
        if A[i]:
            for j in range(i ** 2, n + 1, i):
                A[j] = False
        i += 1
    # calculate sum
    i = 2
    sum = 0
    while i <= n:
        sum += i if A[i] else 0
        i += 1
    return sum
            
if __name__ == "__main__":
    s = time.time()
    print(solve(2 * 10 ** 6))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))