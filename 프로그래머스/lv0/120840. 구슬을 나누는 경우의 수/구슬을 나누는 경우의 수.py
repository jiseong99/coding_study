def fact(a):
    b=1
    while a>1:
        b*=a
        a-=1
    return b

def solution(balls, share):
    answer = fact(balls)/fact(balls-share)/fact(share)
    return int(answer)