import sys
input = sys.stdin.readline

n=int(input())
k=int(input())
spot = sorted(map(int, input().split()))

if n<=k:
    print(0)

else:
    dis=[spot[i+1]-spot[i] for i in range(len(spot)-1)]

    for _ in range(k-1):
        dis.remove(max(dis))

    print(sum(dis))
