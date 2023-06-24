import sys
input = sys.stdin.readline


n=int(input())
a = sorted(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
for i in range(n):
    max_b=max(b)
    x += max_b * a[i]
    b.remove(max_b)

print(x)