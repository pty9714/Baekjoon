C,N=map(int,input().split())
l=[]
for i in range(N):
    cost,p =map(int,input().split())
    l.append([cost,p])

dp=[1e6]*(100+C)
dp[0]=0

for i,j in l:
    for k in range(1,100+C):
        if j<=k:
            dp[k]=min(dp[k],dp[k-j]+i)


print(min(dp[C:]))