def solution(n):
    answer=1
    fact=1
    for i in range(1,n+1):
        answer=i
        fact*=i
        if fact>n:
            answer=i-1
            break

    return answer