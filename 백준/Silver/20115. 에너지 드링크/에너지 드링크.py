import sys
input=sys.stdin.readline

n=int(input())
a=sorted(map(int,input().split()))
print(a[-1]+(sum(a)-a[-1])/2)