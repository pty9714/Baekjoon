from collections import deque
import sys
input = sys.stdin.readline

def dfs(a,visited,l):
    stack = [a]
    visited[a] = 1
    print(a,end= ' ')
    while stack:
        cur = stack.pop()     
        if visited[cur] == 0:
            visited[cur] = 1
            print(cur,end= ' ')
        for i in l[cur]:
            if visited[i] == 0:
                stack.append(i)
                

def bfs(a,visited,l):
    deq = deque([a])
    print(a,end = ' ')
    visited[a] = 1
    while deq:
        cur = deq.popleft()
        for i in l[cur]:
            if visited[i] == 0:
                deq.append(i)
                print(i, end = ' ')
                visited[i] = 1

n,m,r = map(int,input().split())
l = [[] for _ in range(n+1)]
l2 = [[] for _ in range(n+1)]
v1 = [0]*(n+1)
v2 = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)  
for i in range(n+1):
    l[i] = sorted(l[i],reverse=True)
    l2[i] = sorted(l[i])

dfs(r,v1,l)
print()
bfs(r,v2,l2)


