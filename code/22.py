# Project Euler #22 | Sidharth Baskaran | 04/06/2022

import time

def solve():
    with open('project-euler/data/p022_names.txt', 'r') as f:
        lines = sorted([x.strip('"') for x in f.readline().split(',')])
        apb = [chr(x) for x in range(65, 65 + 26)]
        score = 0
        for i, x in enumerate(lines):
            score += sum([apb.index(c) + 1 for c in x]) * (i + 1)
        return score

if __name__ == "__main__":
    s = time.time()
    print(solve())
    e = time.time()
    print('%.3fms' % ((e-s)*1000))