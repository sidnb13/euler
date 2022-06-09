# Project Euler #13 | Sidharth Baskaran | 03/18/2022

import time

def solve():
    with open('project-euler/data/50digits.txt','r') as f:
        msum = 0
        for r in f.readlines():
            msum += int(r.strip('\n'))
        while True:
            if msum // 10 <= 9999999999: # largest 10 digit number
                return msum // 10
            msum = msum // 10
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))