import sys
input = sys.stdin.readline

def get_combinations(coin_values, k):
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coin_values:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]

    return dp[k]

n, k = map(int, input().split())

coin_values = [int(input()) for _ in range(n)]

result = get_combinations(coin_values, k)

print(result)
