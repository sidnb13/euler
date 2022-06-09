# Project Euler #12 | Sidharth Baskaran | 03/18/2022

import time
import math

def brute_force():
    i = 1
    while True:
        curr_sum = i*(i-1)/2
        num_divs = 2 # itself + 1
        div = math.floor(curr_sum/2)
        while div > 1:
            if curr_sum % div == 0:
                num_divs += 1
            div -= 1
        if num_divs > 500:
            return curr_sum
        i += 1
        
def solve():
    # generate a list of primes
    prime_lim = 100000
    A = [True] * (prime_lim + 1)
    i = 2
    while i ** 2 <= prime_lim:
        if A[i]:
            for j in range(i ** 2, prime_lim + 1, i):
                A[j] = False
        i += 1
    
    i = 1
    tri_sum = 0
    while True:
        tri_sum = i*(i+1)/2
        primes = [i for i in range(2, math.ceil(math.sqrt(tri_sum))) if A[i]]
        num_divs = 1
        copy = tri_sum
        for p in primes:
            curr_divs = 0
            while copy % p == 0:
                copy /= p
                curr_divs += 1
            num_divs *= (curr_divs + 1)
        if num_divs >= 500:
            return int(tri_sum)
        i += 1
                
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))