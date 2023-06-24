import sys
input = sys.stdin.readline

n = int(input())
weight = sorted([int(input()) for i in range(n)],reverse=True)
a = len(weight)//3*3
x = sum([weight[i] for i in range(a) if i%3!=2])
y = sum(weight[a:])

print(x+y)
