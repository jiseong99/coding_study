import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst=list(map(int,input().split()))
result=[]

def length():

    def comb(current_comb, remain, num):
        if num == 0:
            result.append(sum(current_comb))
        else:
            for x,y in enumerate(remain):
                updated_comb = current_comb + [y]
                updated_remain = remain[x+1:]
                comb(updated_comb, updated_remain, num - 1)

    for num in range(1, len(lst)+1):
        comb([], lst, num)


length()
answer=0
for x in result:
    if x==m:
        answer+=1

print(answer)