num = int(input())
l = list(map(int,input().split()))
sum = [l[0]]
for i in range(1,num):
    sum.append(max(l[i]+sum[i-1],l[i]))
print(max(sum))