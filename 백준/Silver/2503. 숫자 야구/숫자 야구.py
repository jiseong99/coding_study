#숫자 넣었을때 (n)strike, (m)ball을 문자열로 반환
def baseball(x, y):
    strikes = 0
    balls = 0

    for t in range(3):
        if x[t] == y[t]:
            strikes += 1
        elif x[t] in y:
            balls += 1

    return [str(strikes), str(balls)]

n = int(input())
# 리스트 컴프리헨션 안에서 map쓸때는 list 붙혀야함
a = [list(map(str, input().split())) for _ in range(n)]
answer=0


for i in range(101,1000):
    i=str(i)
    possible = True
    for j in range(n):
        if baseball(i, a[j][0]) != [a[j][1], a[j][2]]:
            possible = False
            break
        for x in range(3):
            if i.count(i[x])>=2 or i[x]=='0':
                possible = False
                break
    if possible:
        answer += 1
        

print(answer)

