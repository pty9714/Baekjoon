a = int(input())
l = []

k = 0
for _ in range(a):
    x,y = map(int,input().split())
    k = max(k,x)
    l.append((x,y))

l = sorted(l,key = lambda x : -x[1])
ans = [0]*(k+1)
for x,y in l:
    for k in range(x,0,-1):
        if ans[k] == 0:
            ans[k] = y
            break
print(sum(ans))
        