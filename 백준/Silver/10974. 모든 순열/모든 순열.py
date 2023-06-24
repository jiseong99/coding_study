import sys
input = sys.stdin.readline

n = int(input())
result=[]
check = [False] * (n+1)


def recur(num):
    if num == n:
        print(' '.join(map(str,result)))
        return

    for i in range(1,n+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recur(num+1)
            check[i]=False
            result.pop()

recur(0)