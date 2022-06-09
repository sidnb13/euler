# Project Euler #67 | Sidharth Baskaran | 02/09/2022

import time

def solve():
    with open('project-euler/data/p067_triangle.txt','r') as f:
        rows = f.readlines()
        rows.reverse()
        rows = [[int(x) for x in r.split(' ')] for r in rows]
        
        for i in range(1, len(rows)):
            for j in range(len(rows[i])):
                rows[i][j] = rows[i][j] + max(rows[i - 1][j], rows[i - 1][j + 1])
        print(rows[len(rows) - 1][len(rows[len(rows) - 1]) - 1])
            
if __name__ == "__main__":
    s = time.time()
    solve()
    e = time.time()
    print('%.3fms' % ((e-s)*1000))