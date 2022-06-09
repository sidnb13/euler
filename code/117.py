# Project Euler #117 | Sidharth Baskaran | 04/15/2022

import time

def count_master_117(units):
    cache = [0] * (units + 1)
    block_sizes = [2, 3, 4]
    def count_ways(spaces):
        if min(block_sizes) > spaces:
            return 0
        if cache[spaces]:
            return cache[spaces]
        res = 0
        for block_size in block_sizes:
            for offset in range(0, spaces - block_size + 1):
                # possible offsets are remaining spaces after inserting 1 block
                res += count_ways(spaces - block_size - offset) + 1 # we insert one more block and apply the offset
        cache[spaces] = res
        return res
    ans = count_ways(units)
    del cache
    return ans

def solve(units):
    return count_master_117(units) + 1

def solve_dp(units):
    dp = [0] * (units + 1)
    dp[2] = 1
    for n in range(3, units + 1):
        dp[n] = 1 + (n - 2) + sum([dp[n-i] for i in range(1, n-1)])
    return dp[units] + 1
            
if __name__ == "__main__":
    s = time.time()
    print(solve(50))
    print(solve_dp(50))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))