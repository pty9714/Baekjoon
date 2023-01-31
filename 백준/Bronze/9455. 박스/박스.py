import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    a,b = map(int,input().split())
    g = []
    for _ in range(a):
        g.append(list(map(int,input().split())))
    total = 0
    for i in range(b):
        box = 0
        for j in range(a-1,-1,-1):
            if g[j][i] == 1:
                total += a-1-j-box
                box +=1   
    print(total)