def prime_num(n):
    a=0
    for i in range(2,n+1):
        if n%i==0:
            a+=1
        else:
            a*=1

    return a

def solution(n):
    answer = []
    for i in range(2,n+1):
        if n%i==0 and prime_num(i)==1:
            answer.append(i)
    return answer