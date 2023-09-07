def solution(s):
    a=s.lower()
    b=a.count('p')
    c=a.count('y')
    return True if b==c else False