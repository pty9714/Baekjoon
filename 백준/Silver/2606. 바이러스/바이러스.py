com = int(input())
num = int(input())
graph = [[]for _ in range(com+1)] 


visited = [False]*(com+1)

def virus(start):
  stack = [start]
  visited[start] = True

  while stack:
    cur = stack.pop()

    for adj in graph[cur]:
      if not visited[adj]:
        visited[adj] = True
        stack.append(adj)

for _ in range(num):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

virus(1)

print(sum(visited)-1)