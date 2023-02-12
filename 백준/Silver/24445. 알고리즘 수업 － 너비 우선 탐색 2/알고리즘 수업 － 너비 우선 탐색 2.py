from collections import deque
import sys
input = sys.stdin.readline

def bfs(a):
    global cnt
    stack = deque([a])
    visited[a] = 1
    while stack:
        cur = stack.popleft()
        for i in l[cur]:
            if visited[i] == 0:
                stack.append(i)
                cnt +=1
                visited[i] = cnt
                
n,m,r = map(int,input().split())
cnt = 1
l = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)  
for i in range(n+1):
    l[i] = sorted(l[i],reverse=True)

bfs(r)
for j in range(1,n+1):
    print(visited[j])
# bfs 데크