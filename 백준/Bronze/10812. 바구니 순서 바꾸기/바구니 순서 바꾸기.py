a,b = map(int,input().split())
l = [i+1 for i in range(a)]
for _ in range(b):
    x,y,z = map(int,input().split())
    l = l[:x-1]+l[z-1:y]+l[x-1:z-1]+l[y:]
print(*l)