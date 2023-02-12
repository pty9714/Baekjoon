
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

def dfs(a):
    global cnt
    visited[a] = cnt
    cnt+=1
    for i in l[a]:
        if visited[i] == 0:
            dfs(i)



n,m,r = map(int,input().split())
cnt = 1
l = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)  
for i in range(n+1):
    l[i] = sorted(l[i])
dfs(r)
for j in range(1,n+1):
    print(visited[j])