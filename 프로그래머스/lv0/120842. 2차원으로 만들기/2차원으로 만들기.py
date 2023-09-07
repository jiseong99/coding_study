def solution(numlist, n):
    answer = []
    array=list(range(0,len(numlist),n))
    for i in array:
        answer.append(numlist[0+i:n+i])
        print(answer)
    return answer