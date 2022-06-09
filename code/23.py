# Project Euler #23 | Sidharth Baskaran | 04/13/2022

import time

def is_abundant(n):
    s = 1
    div = 2
    while div ** 2 <= n:
        if n % div == 0:
            if div == n // div:
                s += div
            else:
                s += div + n // div
        div += 1
    return s > n

def solve():
    lim = 28123
    abundant = [i for i in range(12, lim) if is_abundant(i)] # 0 is not abundant
    bool_res = [i for i in range(lim)]
    
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] < lim:
                bool_res[abundant[i] + abundant[j]] = 0
            else: 
                break
                
    return sum(bool_res)
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))