n,m,k= map(int,input().split())
graph = [[0]*m for _ in range(n)]
mf = 0
for i in range(k):
    a,b= map(int,input().split())
    graph[a-1][b-1] = 1

d = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(x,y):
    global mf
    cnt = 1
    stack = [(x,y)]
    graph[y][x] = 0
    while stack:
        x1,y1 = stack.pop()
        for dx,dy in d:
            mx = x1+dx
            my = y1+dy
            if 0<=mx<m and 0<=my<n:
                if graph[my][mx] == 1:
                    cnt +=1
                    graph[my][mx] = 0
                    stack.append((mx,my))
    if cnt>mf:
        mf = cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(j,i)

print(mf)