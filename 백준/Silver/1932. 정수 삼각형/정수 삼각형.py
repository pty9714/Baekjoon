num = int(input())
l = []
for i in range(num):
    l.append(list(map(int,input().split())))

dp = [[0]*(i+1) for _ in range(num)]
dp[0] = l[0]
for i in range(num-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i][j]+l[i+1][j],dp[i+1][j])
        dp[i+1][j+1] = max(dp[i][j]+l[i+1][j+1],dp[i+1][j+1])

print(max(dp[num-1]))