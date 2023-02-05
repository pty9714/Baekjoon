import math
x1,x2 = map(int,input().split())
y1,y2 = map(int,input().split())

a = x1*y2 + x2*y1
b = x2*y2

g = math.gcd(a,b)
print(a//g, b//g)