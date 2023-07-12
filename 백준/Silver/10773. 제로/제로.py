def push(stack,n):
    stack.append(n)
def pop_a(stack):
    stack.pop()

import sys
input = sys.stdin.readline
n = int(input())
command = []
stack = []
for i in range(n):
    command.append(int(input()))

for i in command:
    if i == 0:
        pop_a(stack)
    else:
        push(stack,i)

print(sum(stack))