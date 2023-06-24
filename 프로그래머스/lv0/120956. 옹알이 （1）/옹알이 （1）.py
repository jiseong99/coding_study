def solution(babbling):
    answer =['aya','ye','woo','ma']
    rep=[]
    for i in babbling:
        for j in answer:
            i=i.replace(j,'*')
        rep.append(i)

    cnt=0
    for i in rep:
        i=set(i)
        if len(i)==1 and '*' in i:
            cnt+=1
    return cnt