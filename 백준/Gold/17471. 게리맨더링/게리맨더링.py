from itertools import combinations
def dfs(l):
    x = l[0]
    stack = [x]
    check = [x]
    while stack:
        s = stack.pop()
        for i in g[s]:
            if i in l and i not in check:
                stack.append(i)
                check.append(i)
    check.sort()
    if l == check:
        return True
    else:
        return False

answer = []
n = int(input())
l = [0]+list(map(int,input().split()))
g = [[] for _ in range(n+1)]
for i in range(n):
    m = list(map(int,input().split()))
    for j in range(1, len(m)):
        g[i+1].append(m[j])

a = [i for i in range(1,n+1)]
for i in range(1,n//2+1):
    combi = combinations(a,i)
    for j in list(combi):
        team1 = []
        team2 = []
        for k in a:
            if k in j:
                team1.append(k)
            else:
                team2.append(k)
        # print(team1)
        # print(team2)
        if dfs(team1) and dfs(team2):

            st1 = 0
            st2 = 0
            for v in team1:
                st1 += l[v]

            for v in team2:
                st2 += l[v]

            answer.append(abs(st1-st2))

if answer:
    print(min(answer))
else:
    print(-1)