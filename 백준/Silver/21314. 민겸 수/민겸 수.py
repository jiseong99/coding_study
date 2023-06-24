import sys
input = sys.stdin.readline
data = str(input())
max = "" 
min = ""
m = 0

for i in range(len(data)):
    if data[i] == 'M':
        m += 1 
    elif data[i] == 'K':
        if m: 
            min += str(10**m + 5) 
            max += str(5 * (10**m))
        else: 
            min += "5" 
            max += "5"
        m = 0
if m: 
    min += str(10 ** (m-1))
    while m:
        max += "1"
        m -= 1
print(max)
print(min)