import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
l = []
for i in range(m):
    l.append(list(map(int, input().strip())))

min_cost = [[float('inf')] * n for _ in range(m)]
min_cost[0][0] = 0

heap = []
heapq.heappush(heap, (0, 0, 0)) 

while heap:
    cost, y, x = heapq.heappop(heap)

    if y == m - 1 and x == n - 1:
        print(cost)
        break

    if cost > min_cost[y][x]:
        continue

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < m and 0 <= nx < n:
            new_cost = cost + (1 if l[ny][nx] == 1 else 0)
            if new_cost < min_cost[ny][nx]:
                min_cost[ny][nx] = new_cost
                heapq.heappush(heap, (new_cost, ny, nx))
