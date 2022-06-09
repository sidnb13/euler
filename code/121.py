# Project Euler #121 | Sidharth Baskaran | 01/25/2022

import time
import math
from itertools import combinations
from functools import reduce
import operator

def solve(n):
    # probabilities of getting blue discs for each turn
    turn_list = [1/z for z in [*range(2,n+2)]]
    # the different winning number possibilities out of given turns n
    prob = 0
    for i in range(math.floor(n/2) + 1, n+1):
        for c in combinations(turn_list, i):
            # probability of getting remaining discs red
            prod_red = math.prod([1 - x for x in list(set(turn_list) - set(c))])
            # probability of getting i blue and n - i red
            prob += reduce(operator.mul, c, 1) * prod_red        
    # expected prize fund
    print(math.floor(1/prob))

if __name__ == "__main__":
    s = time.time()
    solve(15)
    e = time.time()
    print('%.3fms' % ((e-s)*1000))