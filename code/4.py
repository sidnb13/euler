# Project Euler #4 | Sidharth Baskaran | 02/14/2022

import time
import math

# challenge -> solve without string manipulation
def is_palindrome(n):
    c = 0
    n0 = n
    while n0 > 0:
        c += 1
        n0 //= 10    
    for i in range(1, math.ceil(c/2) + 1):
        if n // 10**(c - i) % 10 != n // 10**(i - 1) % 10: # check if ith digit is equal to (c - i + 1)th digit
            return False
    return True

# original inefficient solution
def solve1():
    max_pal = 0
    for f1 in range(999, 99, -1):
        for f2 in range(999, 99, -1):
            if is_palindrome(f1*f2):
                max_pal = max(max_pal, f1* f2)
    print(max_pal)
    
# optimized solution -> much faster
def solve():
    # will always be 3 digit, so hardcoded
    make_pal = lambda n: n * 10**3 + (n % 10) * 10**2 + (n//10 % 10) * 10 + (n//10**2 % 10)
    start = 998
    for i in range(start, 0, -1):
        pal = make_pal(i)
        for j in range(math.floor(math.sqrt(pal)), 0, -1): # largest factor of pal <= sqrt(pal)
            print(pal/j)
            if pal % j == 0 and j < start and pal/j < start:
                return pal
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))