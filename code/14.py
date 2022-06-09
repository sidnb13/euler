# Project Euler #14 | Sidharth Baskaran | 03/19/2022

import time

def solve():
    best_num = 0
    best_len = 0
    for i in range(1, 10 ** 6):
        curr_len = 1
        j = i
        while True:
            if i % 2 == 0:
                i /= 2
            else:
                i = 3*i + 1
            curr_len += 1
            if i == 1:
                break
        if curr_len > best_len:
            best_len = curr_len
            best_num = j
    return best_num
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))