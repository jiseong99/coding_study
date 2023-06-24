import sys
input = sys.stdin.readline

n = int(input())

def answer(n):
    count_five = n // 5
    remain = n % 5

    while count_five >= 0:
        if remain % 3 == 0:

            return count_five + (remain // 3)
        else:
            count_five -= 1
            remain += 5

    return -1

print(answer(n))
