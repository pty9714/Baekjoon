import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
l = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,d = map(int,input().split())
    l[s].append((e,d))

start,end = map(int,input().split())
INF = 10E8
distance = [INF]*(n+1)
def djkstra(start,end):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in l[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    print(distance[end])

djkstra(start,end)