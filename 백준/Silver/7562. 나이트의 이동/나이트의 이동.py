from collections import deque 
for _ in range(int(input())):
    l = int(input())
    k = [[0]*l for _ in range(l)]
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    dx = [2,2,1,1,-1,-1,-2,-2]
    dy = [1,-1,2,-2,2,-2,1,-1]
    def bfs(x,y):
        deq = deque([(x,y)])
        while deq:
            kx,ky = deq.popleft()
            if kx == ex and ky == ey:
                break
            for i in range(8):
                mx = kx+dx[i]
                my = ky+dy[i]
                if 0<=mx<l and 0<=my<l and k[mx][my] == 0:
                    k[mx][my] = k[kx][ky]+1
                    deq.append((mx,my))
    bfs(sx,sy)
    print(k[ex][ey])