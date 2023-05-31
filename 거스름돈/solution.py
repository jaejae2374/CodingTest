def solution(n, money):
    dp = [1] + [0] * n

    for coin in sorted(money):
        for price in range(coin, n+1):
            dp[price] = (dp[price] + dp[price - coin]) % 1000000007
    return dp[n]
