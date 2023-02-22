a,b = map(int,input().split())
l = [i+1 for i in range(a)]
for _ in range(b):
    x,y= map(int,input().split())
    l[x-1], l[y-1] = l[y-1],l[x-1]

print(*l)