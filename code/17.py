# Project Euler #17 | Sidharth Baskaran | 03/21/2022

import time

NUMBERS = [(len(x), x) for x in ['one', 'two', 'three', 'four', 'five', 'six', 
           'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
           'nineteen','twenty']]
TENS_20 = [(len(x), x) for x in ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']]

DBG = True

def solve(n):
    lens = 0
            
    for j in range(1, n + 1):
        i = j % 100
        
        if DBG:
            print('---------')
                
        if i > 0:
            if i < 20:
                lens += NUMBERS[i - 1][0]
                if DBG:
                    print(j, NUMBERS[i - 1][1])
            elif i >= 20 and i < 30:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 20 - 1][0]) + TENS_20[0][0]
                if DBG:
                    print(j, TENS_20[0][1] + '-' +  ('' if i % 10 == 0 else NUMBERS[i - 20 - 1][1]))
            elif i >= 30 and i < 40:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 30 - 1][0]) + TENS_20[1][0]
                if DBG:
                    print(j, TENS_20[1][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 30 - 1][1]))
            elif i >= 40 and i < 50:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 40 - 1][0]) + TENS_20[2][0]
                if DBG:
                    print(j, TENS_20[2][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 40 - 1][1]))
            elif i >= 50 and i < 60:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 50 - 1][0]) + TENS_20[3][0]
                if DBG:
                    print(j, TENS_20[3][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 50 - 1][1]))
            elif i >= 60 and i < 70:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 60 - 1][0]) + TENS_20[4][0]
                if DBG:
                    print(j, TENS_20[4][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 60 - 1][1]))
            elif i >= 70 and i < 80:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 70 - 1][0]) + TENS_20[5][0]
                if DBG:
                    print(j, TENS_20[5][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 70 - 1][1]))
            elif i >= 80 and i < 90:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 80 - 1][0]) + TENS_20[6][0]
                if DBG:
                    print(j, TENS_20[6][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 80 - 1][1]))
            elif i >= 90 and i < 100:
                lens += (0 if i % 10 == 0 else NUMBERS[i - 90 - 1][0]) + TENS_20[7][0]
                if DBG:
                    print(j, TENS_20[7][1] + '-' + ('' if i % 10 == 0 else NUMBERS[i - 90 - 1][1]))
            
        if j >= 100 and j < 1000:
            lens += NUMBERS[j // 100 - 1][0] + len('hundred')
            if j % 100 != 0:
                lens += len('and')
            if DBG:
                print(j, NUMBERS[j // 100 - 1][1] + ' hundred and' if j % 100 != 0  else NUMBERS[j // 100 - 1][1] + ' hundred')
                
    if n == 1000:
        lens += len('onethousand')
                
    return lens
            
if __name__ == "__main__":
    s = time.time()
    print(solve(1000))
    e = time.time()
    print('%.3fms' % ((e-s)*1000))