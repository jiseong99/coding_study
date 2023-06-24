n=int(input())
tip=[int(input()) for _ in range(n)]
tip.sort(reverse=True)
real_tip=[tip[i]-i for i in range(n)]
get_money=[i for i in real_tip if i>=0]
print(sum(get_money))
