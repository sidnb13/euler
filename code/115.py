# Project Euler #115 | Sidharth Baskaran | 04/15/2022

import time

def fill(m, n, cache):
    block_sizes = list(range(m, n + 1))
    def count(spaces):
        if min(block_sizes) > spaces:
            return 0
        if cache[spaces]:
            return cache[spaces]
        res = 0
        for block_size in block_sizes:
            for offset in range(0, spaces - block_size + 1):
                res += count(spaces - block_size - offset - 1) + 1
        cache[spaces] = res
        return res
    return count(n) + 1, cache

def solve():
    m = 50
    n = 50
    cache = [0] * (n + 1)
    sol, cache = fill(m, n, cache)
    while sol < 1e6:
        sol, cache = fill(m, n, cache + [0])
        n += 1
    return n - 1
            
if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))