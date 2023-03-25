import sys
input=sys.stdin.readline
import itertools
num = int(input())
people=[i for i in range(num)] 
graph = []
for i in range(num):
    graph.append(list(map(int,input().split())))
res = 100*num*num
       
team = list(itertools.combinations(people,num//2))
for t in team:
    start = 0
    link = 0
    nt = [x for x in range(num) if x not in t]
    for i in t:
        for j in t:
            start += graph[i][j]
    
    for i in nt:
        for j in nt:
            link += graph[i][j]

    res = min(res, abs(start-link))

print(res)