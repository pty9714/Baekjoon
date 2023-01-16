#2506
num = int(input())
l = list(map(int,input().split()))
sum = 0
cnt = 0
for i in l:
    if i == 1:
        cnt+=1
        sum+=cnt
    else:
        cnt = 0
print(sum)