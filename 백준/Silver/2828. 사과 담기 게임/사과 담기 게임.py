a, b = map(int, input().split())
c = int(input())
apple = []
for i in range(c):
    apple.append(int(input()))
move = 0
end = b
start = 1
for x in apple:
    if(end >= x and start <= x):
        continue
    elif (end < x):
        move += x - end
        end = x
        start = x - (b - 1)
    elif (start > x):
        move += start - x
        start = x
        end = x + (b - 1)
print(move)