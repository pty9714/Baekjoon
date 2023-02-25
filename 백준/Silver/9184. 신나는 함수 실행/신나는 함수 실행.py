import sys
input = sys.stdin.readline
dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]
def w1(a,b,c):
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i <= 0 or j <= 0 or k <= 0:
                    dp[i][j][k] = 1
                elif i<j and j<k:
                    dp[i][j][k] = dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]                 
                    
    return(dp[a][b][c])

while True:
    x,y,z = map(int,input().split())
    if x == -1 and y == -1 and z== -1:
        break
    elif x <= 0 or y <= 0 or z <= 0:
        print(f'w({x}, {y}, {z}) = 1')
        continue
    elif x>20 or y>20 or z>20:
        print(f'w({x}, {y}, {z}) = {w1(20,20,20)}')
        continue

    print(f'w({x}, {y}, {z}) = {w1(x,y,z)}')