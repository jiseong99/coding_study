def solution(n, m):
    answer = []
    s = min(n,m)
    max_div = 0
    min_mult = 0
    for i in range(s,0,-1):
        if n % i == 0 and m % i == 0:
            max_div = i
            break
    
    min_mult = (n/max_div * m/max_div * max_div)
    
    answer.append(int(max_div))
    answer.append(int(min_mult))
    return answer