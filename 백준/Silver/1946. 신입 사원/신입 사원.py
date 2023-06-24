import sys

input = sys.stdin.readline

a = int(input())
for i in range(a):
    n = int(input())
    score = []

    for j in range(n):
        x, y = map(int, input().split())
        score.append((x, y))
    sort_score=sorted(score)

    count=1
    ind=0
    for i in range(1,len(sort_score)):
        if sort_score[i][1]<sort_score[ind][1]:
            count+=1
            ind=i

    print(count)