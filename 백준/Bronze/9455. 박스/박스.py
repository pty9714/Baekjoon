import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    a,b = map(int,input().split())
    g = []
    cnt = -1
    total = 0
    for _ in range(a):
        g.append(list(map(int,input().split())))
    while cnt != 0:
        cnt = 0
        for i in range(a-1,0,-1):
            for j in range(b-1,-1,-1):
                if g[i][j] == 0 and g[i-1][j] == 1:
                    g[i][j] = 1
                    g[i-1][j] = 0
                    cnt+=1

        total +=cnt
    
    print(total)