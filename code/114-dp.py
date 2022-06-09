import time

def solve114(units):
    # DP solution without recursion
    dp = [0] * (units + 1)
    # we know base case
    dp[3] = 1
    for n in range(4, units + 1):
        dp[n] = sum(
            [sum([dp[n - k - i - 1] + 1 for i in range(0, n-k + 1) ]) for k in range(3, n + 1)]
        )
    return dp[units] + 1

def solve115():
    m = 50
    n = 50
    # DP solution without recursion
    def helper(units):
        dp = [0] * (units + 1)
        # we know base case
        dp[m] = 1
        for n in range(m + 1, units + 1):
            dp[n] = sum(
                [sum([dp[n - k - i - 1] + 1 for i in range(0, n-k + 1) ]) for k in range(m, n + 1)]
            )
        return dp[units] + 1
    sol = helper(n)
    while sol < 1e6:
        sol = helper(n)
        n += 1
    return n - 1

def solve116(units):
    def helper(m):
        # DP solution without recursion
        dp = [0] * (units + 1)
        # we know base case
        dp[m] = 1
        for n in range(m + 1, units + 1):
            dp[n] = sum([dp[n - m - i] + 1 for i in range(0, n-m + 1)])
        return dp[units] + 1
    return sum([helper(m) for m in [2,3,4]])

def solve117(units):
    # DP solution without recursion
    dp = [0] * (units + 1)
    # we know base case
    dp[2] = 1
    for n in range(3, units + 1):
        dp[n] = sum(
            [sum([dp[n - k - i] + 1 for i in range(0, n-k + 1) ]) for k in [2,3,4]]
        )
    return dp[units] + 1

if __name__ == "__main__":
    # Evidence that DP is faster
    s = [time.time()]
    print(solve114(50))
    s.append(time.time())
    print(solve115())
    s.append(time.time())
    print(solve116(50))
    s.append(time.time())
    print(solve117(50))
    s.append(time.time())
    
    print(['%.3fms' % ((s[i+1]-s[i])*1000) for i in range(len(s) - 1)])