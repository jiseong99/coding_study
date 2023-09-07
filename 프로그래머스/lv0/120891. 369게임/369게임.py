def solution(order):
    answer = 0
    a=['3','6','9']
    str_order=str(order)
    str_order.split()
    for i in str_order:
        if i in a:
            answer+=1
    return answer