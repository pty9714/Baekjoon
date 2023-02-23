from collections import deque

a,b = map(int,input().split())
cnt = 0
Q = deque([4,7])
while Q:
    q = Q.popleft()
    Q.append(q*10+4)
    Q.append(q*10+7)
    if a<=q<=b:
        cnt+=1
    if b<q:
        break
print(cnt)