import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def combinations(n, lst):
    answer = []
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p1 = p2 = p3 = p4 = 1
                for q in lst[:i]:
                    p1 *= q
                for w in lst[i:j]:
                    p2 *= w
                for e in lst[j:k]:
                    p3 *= e
                for t in lst[k:]:
                    p4 *= t
                answer.append(p1 + p2 + p3 + p4)
    return max(answer)

result = combinations(n, lst)
print(result)