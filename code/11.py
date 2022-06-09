# Project Euler #11 | Sidharth Baskaran | 03/18/2022

import time

def solve():
    with open('project-euler/data/grid.txt','r') as f:
        rows = f.readlines()
        grid = [[int(x) for x in r.split(' ')] for r in rows]
        best_prod = 1
        for i in range(16):
            for j in range(16):
                if i + 3 < 20 and j + 3 < 20:
                    best_prod = max(best_prod, grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])
                if i - 3 >= 0 and j + 3 < 20:
                    best_prod = max(best_prod, grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3])
                if i + 3 < 20:
                    best_prod = max(best_prod, grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j])
                if j + 3 < 20:
                    best_prod = max(best_prod, grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])
                
if __name__ == "__main__":
    s = time.time()
    solve()
    e = time.time()
    print('%.3fms' % ((e-s)*1000))