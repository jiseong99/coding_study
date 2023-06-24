import sys
intput=sys.stdin.readline

n=int(input())
weight=sorted(map(int,input().split()))
a=0
if len(weight)%2==1:
    a = weight.pop(-1)
b = [weight[i] + weight[-i-1] for i in range(len(weight)//2)]
b.append(a)
print(max(b))