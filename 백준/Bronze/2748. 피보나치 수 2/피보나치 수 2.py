import sys
input = sys.stdin.readline


def fibonacci(n):
    dp = [1] * (n + 1)
    dp[0] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


n = int(input())

print(fibonacci(n))
