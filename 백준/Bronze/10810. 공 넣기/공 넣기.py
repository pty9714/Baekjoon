
a,b = map(int,input().split())
l = [0]*a
for _ in range(b):
    x,y,z = map(int,input().split())
    for i in range(x-1,y):
        l[i] = z

print(*l)