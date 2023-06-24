N, K = map(int, input().split())
h = list(map(int, input().split()))

arr=[h[i+1]-h[i] for i in range(N-1)]

arr.sort()
cost = 0

for i in range(N - K):
    cost += arr[i]

print(cost)