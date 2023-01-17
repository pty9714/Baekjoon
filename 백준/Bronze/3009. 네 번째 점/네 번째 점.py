x0 = 0
y0 = 0
for i in range(3):
    x,y = map(int,input().split())
    x0 ^= x
    y0 ^= y
print(x0,y0)