import sys
input = sys.stdin.readline

n = int(input())
profile = []

for i in range(n):
    x, y = map(int, input().split())
    profile.append((x, y))

answer=[]
for i in range(n):
    count = 0
    for j in range(n):
        if profile[i][0] < profile[j][0] and profile[i][1] < profile[j][1]:
            count += 1
    answer.append(count + 1)

print(*answer)