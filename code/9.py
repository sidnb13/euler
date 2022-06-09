# Project Euler #9 | Sidharth Baskaran | 01/21/2022

import time
import math

def solve(k):
    for c in range(math.ceil(k/3), math.ceil(k/2)):
        for b in range(math.ceil((k-c)/2), math.ceil(k/2)):
            a = k - (b + c)
            if a**2 + b**2 == c**2:
                return a*b*c
            
if __name__ == "__main__":
    s = time.time()
    print(solve(1000))
    e = time.time()

    print('%.3fms' % ((e-s)*1000))