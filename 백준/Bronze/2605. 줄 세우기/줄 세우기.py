num = int(input())
l = list(map(int,input().split()))
ans = []
for i in range(1,num+1):
    v = i-1-l[i-1]
    ans1 = ans[:v]
    ans2 = ans[v:]
    ans1.append(i)
    ans = ans1+ans2
print(*ans)