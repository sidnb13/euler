# Project Euler #20 | Sidharth Baskaran | 03/22/2022

import time
import math

def solve(n):
    # count number of multiple 5s in n, all combinations of even odd <= n create multiple of 5
    res = 1
    count = 0
    
    while res*5 <= n:
        res *= 5
        count += math.floor(n/res)
    
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
        
    fact //= 10 ** count
    
    sum_digits = 0
    while fact > 0:
        sum_digits += fact % 10
        fact //= 10
    return sum_digits
            
if __name__ == "__main__":
    s = time.time()
    print(solve(100))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))