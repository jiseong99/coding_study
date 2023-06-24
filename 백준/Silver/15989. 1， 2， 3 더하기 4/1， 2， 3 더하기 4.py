import sys
input = sys.stdin.readline

def answer(t, numbers):
    dp = [1] * 10001

    for i in range(2, 10001):
        dp[i] += dp[i - 2]

    for i in range(3, 10001):
        dp[i] += dp[i - 3]

    result = []
    for n in numbers:
        result.append(dp[n])

    for res in result:
        print(res)

t = int(input())
numbers = [int(input()) for _ in range(t)]

answer(t, numbers)