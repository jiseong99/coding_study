n=int(input())
weight=[]
answer=[]
for i in range(n):
    weight.append(int(input()))
weight.sort(reverse=True)
for i in range(n):
    answer.append(weight[i]*(i+1))
print(max(answer))