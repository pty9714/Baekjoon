n = int(input())
l = []
k = 0
for i in range(n):
    a,b = map(int,input().split())
    k = max(k,a)
    l.append((a,b))
answer = [0]*k

l.sort(key=lambda x: (-x[1],x[0]))

for i in l:
    for j in range(i[0]-1,-1,-1):
        if not answer[j]:
            answer[j] = i[1]
            break
print(sum(answer))