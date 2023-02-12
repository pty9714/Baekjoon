import sys
input = sys.stdin.readline

def dfs(a):
    global cnt
    stack = [a]

    while stack:
        cur = stack.pop()
        if visited[cur] == 0:
            cnt +=1
            visited[cur] = cnt
        for i in l[cur]:
            if visited[i] == 0:
                stack.append(i)
                

n,m,r = map(int,input().split())
cnt = 0
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