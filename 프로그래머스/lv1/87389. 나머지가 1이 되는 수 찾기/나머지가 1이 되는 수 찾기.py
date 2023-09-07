def solution(n):
    answer=0
    b=1
    while b<n:
        if n%b==1:
            answer=b
            break
        b+=1
        
    return answer