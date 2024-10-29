n = int(input())
c = [0]*366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        c[i] += 1

row = 0 
col = 0 
answer = 0
for day in c:
    if day != 0:
        col = max(col, day)
        row += 1
    else: 
        answer += row * col
        row = 0
        col = 0
answer += row * col
print(answer)