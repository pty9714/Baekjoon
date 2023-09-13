from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
m,n = map(int, input().split())
l = [list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]  # 가중치

q = deque()
q.append((0,0))
dist[0][0] = 0
while q:
    x,y = q.popleft()
    for k in range(4):
        mx = x + dx[k]
        my = y + dy[k]
        if 0 <= mx < m and 0 <= my < n:
            if dist[my][mx] == -1:
                if l[my][mx] == 0:
                    dist[my][mx] = dist[y][x]
                    q.appendleft((mx, my))
                else:
                    dist[my][mx] = dist[y][x] + 1
                    q.append((mx, my))
print(dist[n-1][m-1])