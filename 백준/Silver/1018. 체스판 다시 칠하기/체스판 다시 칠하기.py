import sys
input = sys.stdin.readline


n, m = map(int, input().split())

chess = [input() for _ in range(n)]
count = []

for a in range(n-7):
    for b in range(m-7):
        x = 0
        y = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        x += 1
                    if chess[i][j] != 'B':
                        y += 1
                else:
                    if chess[i][j] != 'B':
                        x += 1
                    if chess[i][j] != 'W':
                        y += 1
        count.append(min(x, y))

print(min(count))