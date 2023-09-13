def solution(s):
    front = ''
    tail = ''
    for i in s:
        if i.isupper() == True:
            tail += i
        else:
            front += i
    answer_lst = sorted(front, reverse = True) + sorted(tail, reverse = True)
    result = ""
    for s in answer_lst:
        result += s
    return str(result.strip())
