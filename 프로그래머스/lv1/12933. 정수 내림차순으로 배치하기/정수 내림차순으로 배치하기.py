def solution(n):
    answer = []
    ans=''
    s = str(n)
    for i in range(1, len(s) + 1):
        answer.append(int(s[-i]))
    b=sorted(answer,reverse=True)
    for i in range(len(b)):
        ans+=str(b[i])
    return int(ans)
