# Project Euler #19 | Sidharth Baskaran | 03/22/2022

import time

isLeap = lambda yr: (yr % 100 != 0 and yr % 4 == 0) or yr % 400 == 0
MONTHS = lambda yr: [31, 29 if isLeap(yr) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solve():
    st_yr = 1900
    weekday = 0 # start on monday
    count = 0

    for yr in range(st_yr, 2001):
        for num_days in MONTHS(yr):
            for d in range(num_days):
                if weekday == 6 and d == 0 and yr >= 1901:
                    count += 1
                weekday = (weekday + 1) % 7
                
    return count
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))