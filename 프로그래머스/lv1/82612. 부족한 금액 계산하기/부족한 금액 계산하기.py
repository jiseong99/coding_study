def solution(price, money, count):
    a = 0
    x = 0
    for i in range(1,count + 1):
        x += price
        a += x
    
    return (a - money) if (a - money) > 0 else 0 