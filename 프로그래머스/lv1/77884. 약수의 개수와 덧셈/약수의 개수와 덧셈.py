def solution(left, right):
    answer = 0
    l_r = [_ for _ in range(left, right + 1)]

    for i in l_r:
        a = 0
        for j in range(1,i + 1):
            if i % j == 0:
                a += 1
            else:
                continue
        if a % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer