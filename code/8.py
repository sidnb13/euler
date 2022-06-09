# Project Euler #8 | Sidharth Baskaran | 03/19/2022

import time

def solve():
    with open('project-euler/data/largenum.txt','r') as f:
        digits = []        
        for r in f.readlines():
            for x in r.strip('\n'):
                digits.append(int(x))
        
        best_prod = 1
        for i in range(1000 - 13):
            curr_prod = 1
            for j in range(i, i + 13):
                curr_prod *= digits[j]
            best_prod = max(curr_prod, best_prod)
        
        return best_prod
            
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))