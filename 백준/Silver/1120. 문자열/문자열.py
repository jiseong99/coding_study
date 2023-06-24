import sys
input = sys.stdin.readline


a, b = map(str, input().split())
lst = []
diff = len(b)-len(a)

for j in range(diff+1):
    answer=0
    for i in range(len(a)):
        if a[i] != b[i+j]:
            answer += 1
    lst.append(answer)
print(min(lst))