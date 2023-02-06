while True:
  a,b = map(int,input().split())
  if a == 0 and b == 0 :
    break

  di = [-1,0,1]
  d = [(x,y) for x in di for y in di]
  d.remove((0,0))


  check = [False] *(a*b +1)
  graph = [[] for _ in range(a*b +1)]
  l=[]
  for _ in range(b):
    l.append(list(map(int,input().split())))

  for i in range(b):
    for j in range(a):
      if l[i][j] == 1:
        graph[i*a+(j+1)].append(i*a+(j+1))
        for k in d:
          dx,dy = k
          try:
            if i+dx>=0 and j+dy>=0:
              if l[i+dx][j+dy] == 1:
                graph[i*a+(j+1)].append((i+dx)*a+j+dy+1)
          except:
            continue

  cnt = 0
  def virus(start):
    if graph[start] != [] and check[start] == False :
      stack = [start]
      check[start] = True

      while stack:
        cur = stack.pop()

        for adj in graph[cur]:
          if not check[adj]:
            check[adj] = True
            stack.append(adj)
      else:
        global cnt
        cnt += 1
  for p in range(1,a*b+1):
    virus(p)
  print(cnt)