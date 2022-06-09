# Project Euler #54 | Sidharth Baskaran | 01/13/2022

import time, re
import numpy as np
from collections import Counter

RANKS = dict(zip(['hc','1p','2p','3k','s','f','fh','4k','sf','rf'],[*range(1,11)]))
VALUES = dict(zip(['2','3','4','5','6','7','8','9','T','J','Q','K','A'], [*range(2,15)]))

def score_hand(raw_data, db=False):
    # separate values and suit string lists
    values = [s[0] for s in raw_data]
    suits = [s[1] for s in raw_data]
    # get frequency of suits and values
    freq_s = Counter(suits)
    freq_v = Counter(values)
    card_scores = [VALUES[x] for x in values]
    # zip suits, values, evaluation metric (score)
    hand_uns = list(zip(suits ,values, card_scores))
    # conditions to check
    conditions = [
        lambda: RANKS['hc'],
        lambda: RANKS['1p'] if 2 in list(freq_v.values()) else 0,
        lambda: RANKS['2p'] if list(freq_v.values()).count(2) >= 2 else 0,
        lambda: RANKS['3k'] if 3 in list(freq_v.values()) else 0,
        lambda: RANKS['s'] if sum(np.diff(sorted([c for _,_,c in hand_uns])) == [1] * 4) == 4 else 0,
        lambda: RANKS['f'] if len(freq_s.keys()) == 1 else 0,
        lambda: RANKS['fh'] if 2 in list(freq_v.values()) and 3 in list(freq_v.values()) else 0,
        lambda: RANKS['4k'] if 4 in list(freq_v.values()) else 0,
        lambda: RANKS['sf'] if sum(np.diff(sorted([c for _,_,c in hand_uns])) == [1] * 4) == 4 and len(freq_s.keys()) == 1 else 0,
        lambda: RANKS['rf'] if sorted(['T','J','K','Q','A']) == sorted(values) else 0
    ]
    # populate the gained scores
    score_conditions = [c() for c in conditions]
    # set the highest rank attained as the score
    score = (score_conditions[i] for i in range(len(conditions) - 1, -1, -1) if score_conditions[i] > 0)
    ret = (next(score), score_conditions, card_scores, sorted(values),  freq_v)
    if db:
        print(ret)
    return ret

def solve():
    raw = open('project-euler/data/p054_poker.txt','r').readlines()
    score = 0
    for line in raw:
        split = re.split(r'\s', line)[:-1]
        sc1, r1, scores1, vals1, f1 = score_hand(split[:5])
        sc2, r2, scores2, vals2, f2 = score_hand(split[5:])
        if sc1 == sc2:
            p1 = [r1[7], r1[6], r1[3], r1[2], r1[1]]
            p2 = [r2[7], r2[6], r2[3], r2[2], r2[1]]
            if sum(p1) == sum(p2) and sum(p1) > 0: # paired case, get highest value of paired numbers
                for k1,k2 in zip(f1.keys(), f2.keys()):
                    # remove single-count keys to leave pairs
                    if f1[k1] == 1:
                        vals1.remove(k1)
                    if f2[k2] == 1:
                        vals2.remove(k2)
                # get highest of paired values            
                highest_pair_val1 = max([VALUES[v] for v in set(vals1)])
                highest_pair_val2 = max([VALUES[v] for v in set(vals2)])
                if highest_pair_val1 == highest_pair_val2:
                    score += max(scores1) > max(scores2)
                else:
                    score += highest_pair_val1 > highest_pair_val2
            else:
                # check for max value card
                score += max(scores1) > max(scores2)
        elif sc1 > sc2:
            score += 1
    print(score)
    
if __name__ == "__main__":
    s = time.time()
    solve()
    e = time.time()
    print('%.3fms' % ((e-s)*1000))