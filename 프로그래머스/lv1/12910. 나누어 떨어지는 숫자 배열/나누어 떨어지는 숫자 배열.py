def solution(arr, divisor):
    answer = []
    arr.sort()
    for x in arr:
        if x%divisor==0:
            answer.append(x)
    return answer if len(answer)!=0 else [-1]