

def bfs(start, end, maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [start]
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps) :
                if visited[ny][nx] == 0 and maps[ny][nx] != 'X':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx,ny))

    return visited[end[1]][end[0]] 

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = (j,i)
            
            if maps[i][j] == 'E':
                e = (j,i)
            
            if maps[i][j] == 'L':
                l = (j,i)

    a1 = bfs(s,l,maps)
    a2 = bfs(l,e,maps)
    if a1 == 0 or a2 == 0:
        return -1
    else:
        return a1+a2