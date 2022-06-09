# Project Euler #50 | Sidharth Baskaran | 01/09/2022

import time
import math

def is_prime(n):
    for x in range(math.ceil(math.sqrt(n)),1,-1):
        if n % x == 0:
            return False
    return True

def get_prime_list(n):    
    # boolean array
    A = [True] * (n + 1)
    # sieve of Erastothenes
    i = 2
    while i**2 <= n:
        if A[i]:
            for j in range(i**2, n + 1, i):
                A[j] = False
        i += 1
    
    # get list of primes
    primes = []
    for i in range(len(A)):
        if A[i]:
            primes.append(i)
    return primes[2:]
    
def solve(n):
    # get the largest sublist possible
    prime_list = get_prime_list(n)
    s = 0
    max_sub_len = 0
    for x in prime_list:
        if s >= n:
            break
        s += x
        max_sub_len += 1
    
    # iterate through sublist-offset combinations
    offset = 0
    max_len = 0
    best_sum = s
    
    while max_sub_len - offset > max_len:
        curr_len = max_sub_len - offset
        while curr_len > max_len:
            curr_sum = sum(prime_list[offset:offset+curr_len])
            if is_prime(curr_sum):
                max_len = curr_len
                best_sum = curr_sum
            curr_len -= 1
        offset += 1
                
    print(best_sum)

if __name__ == "__main__":
    s = time.time()
    solve(1000000)
    e = time.time()

    print('%.3fms' % ((e-s)*1000))