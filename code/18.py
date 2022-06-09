# Project Euler #18 | Sidharth Baskaran | 03/21/2022

import time

def solve():
    with open('project-euler/data/triangle.txt', 'r') as f:
        grid = []
        for r in f.readlines():
            grid.append([int(x) for x in r.split(' ')])
        # DP soln
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[i])):
                grid[i][j] += max(grid[i+1][j], grid[i+1][j+1])
                
        return grid[0][0]
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))