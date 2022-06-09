# Project Euler #15 | Sidharth Baskaran | 03/19/2022

import time
from math import factorial

# solution using DP, subproblem of num paths from a vertex
def solveDP(n):
    grid = [[0] * n + [1] for _ in range(n)] + [[1] * (n + 1)]
        
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    
    return grid[0][0]

# simple combinatorics of n choose 2n
def solve(n):
    return factorial(2*n) // (factorial(n) ** 2)
            
if __name__ == "__main__":
    s = time.time()
    dpsol = solveDP(20)
    sol = solve(20)
    print(dpsol)
    print(sol)
    print(sol == dpsol)
    e = time.time()
    print('%.3fms' % ((e-s)*1000))