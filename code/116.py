# Project Euler #116 | Sidharth Baskaran | 04/14/2022

import time

def count_master_116(units, block_size):
    cache = [0] * (units + 1)
    def count_ways(spaces, block_size):
        if block_size > spaces:
            return 0
        if cache[spaces]:
            return cache[spaces]
        res = 0
        for offset in range(0, spaces - block_size + 1): 
            # possible offsets are remaining spaces after inserting 1 block (so add 1)
            res += count_ways(spaces - block_size - offset, block_size) + 1 # we insert one more block and apply the offset
        cache[spaces] = res
        return res
    ans = count_ways(units, block_size)
    del cache
    return ans

def solve(units):
    return sum([count_master_116(units, i) for i in [2, 3, 4]])
    
if __name__ == "__main__":
    s = time.time()
    print(solve(50))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))