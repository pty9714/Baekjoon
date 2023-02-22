a,b = map(int,input().split())
l = [i+1 for i in range(a)]
for _ in range(b):
    x,y= map(int,input().split())
    k = l[x-1:y]
    for i in range(x-1,y):
        l[i] = k[y-1-i]
        

print(*l)