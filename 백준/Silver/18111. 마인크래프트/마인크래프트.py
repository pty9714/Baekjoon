import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
g = []

for _ in range(n):
    l = list(map(int,input().split()))
    g.append(l)

ans_time = 500*500*256
ans_height = 0
for i in range(257):
    plus_block = 0
    minus_block = 0
    for j in range(n):
        for k in range(m):
            if g[j][k] > i:
                plus_block += g[j][k] -i
            else:
                minus_block +=i-g[j][k]
    
    if b+plus_block-minus_block>=0:
        if ans_time>=plus_block*2+minus_block:
            ans_time = plus_block*2+minus_block
            ans_height = i
        else:
            break
print(ans_time,ans_height)
