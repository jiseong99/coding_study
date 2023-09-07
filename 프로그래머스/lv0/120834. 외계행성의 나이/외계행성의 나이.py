def solution(age):
    answer=''
    sibal = {0:'a' , 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    aage=str(age)

    for i in range(len(aage)):
        answer+=sibal.get(int(aage[i]))

    return answer