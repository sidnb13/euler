# Project Euler #16 | Sidharth Baskaran | 03/21/2022

import time

def solve(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
            
if __name__ == "__main__":
    s = time.time()
    print(solve(2 ** 1000))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))