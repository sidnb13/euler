# Project Euler #6 | Sidharth Baskaran | 03/19/2022

import time

def solve(n):
    return int( (n*(n+1)/2) ** 2 - (n**3/3 + 3*n*(n+1)/6 - n/3) )
            
if __name__ == "__main__":
    s = time.time()
    print(solve(100))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))