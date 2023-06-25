import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = lst[0]

if n > 1:
    dp[1] = lst[0] + lst[1]

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + lst[i], dp[i - 3] + lst[i - 1] + lst[i])

print(dp[n - 1])
