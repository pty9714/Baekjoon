from collections import deque

a,b = map(int,input().split())
graph = []
for _ in range(a):
    graph.append(list(map(int,input())))
d = [(0,1),(0,-1),(1,0),(-1,0)]
graph[0][0] = 0


deq = deque([(0,0,1)])     
def bfs():
    while deque:
        cur_x,cur_y,cnt=deq.popleft()
        if cur_x == b-1 and cur_y == a-1:
            print(cnt)
            break
        for dt in d:
            dx,dy = dt
            mx = cur_x+dx
            my = cur_y+dy
            if 0<=mx<=b-1 and 0<=my<=a-1:
                if graph[my][mx] == 1:
                    graph[my][mx] = 0
                    k=cnt+1
                    deq.append((mx,my,k))
        
bfs() 