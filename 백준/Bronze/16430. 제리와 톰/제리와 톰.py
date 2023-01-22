import math
a,b = map(int,input().split())
a= b-a
c= math.gcd(a,b)
print(a//c,b//c)