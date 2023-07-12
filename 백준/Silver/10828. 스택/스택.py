def push(lst, n):
    lst = lst.append(n)

def pop_a(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])
        lst.pop(-1)
def size(lst):
    print(len(lst))
def empty(lst):
    print(1) if len(lst) == 0 else print(0)
def top(lst):
    print(-1) if len(lst) == 0 else print(lst[-1])

import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(stack,command[1])
    elif command[0] == 'pop':
        pop_a(stack)
    elif command[0] == 'size':
        size(stack)
    elif command[0] == 'empty':
        empty(stack)
    elif command[0] == 'top':
        top(stack)