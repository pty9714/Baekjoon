l = 0
m = 0
for i in range(4):
    a,b=map(int,input().split())
    l = l+b-a
    if l>m:
        m = l

print(m)