def solution(absolutes, signs):
    a=0
    for i in range(len(absolutes)):
        if signs[i]==True:
            a+=absolutes[i]
        else:
            a-=absolutes[i]
    return a