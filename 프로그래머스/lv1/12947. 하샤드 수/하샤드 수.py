def solution(x):
    a = []
    s=str(x)
    b=0
    for i in range(len(s)):
        a.append(s[i])
    for i in range(len(a)):
        b+=int(a[i])
    return True if x%b==0 else False