# Project Euler #114 | Sidharth Baskaran | 04/15/2022

import time

def solve(units):
    cache = [0] * (units + 1)
    def count(spaces):
        if spaces < 3:
            return 0
        if cache[spaces]:
            return cache[spaces]
        res = 0
        for block_size in range(3, spaces + 1):
            for offset in range(0, spaces - block_size + 1):
                res += count(spaces - block_size - offset - 1) + 1
        cache[spaces] = res
        return res
    return count(units) + 1

def solve_dp(units):
    # DP solution without recursion
    dp = [0] * (units + 1)
    # we know base case
    dp[3] = 1
    for n in range(4, units + 1):
        dp[n] = sum(
            [sum([dp[n - k - i - 1] + 1 for k in range(3, n-i + 1)]) for i in range(0, n + 1)]
        )
    return dp[units] + 1
    
if __name__ == "__main__":
    # Evidence that DP is faster
    s = time.time()
    print(solve(50))
    i = time.time()
    print('%.3fms' % ((i-s)*1000))
    print(solve_dp(50))
    e = time.time()
    print('%.3fms' % ((e-i)*1000))