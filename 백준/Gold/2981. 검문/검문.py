import sys
import math
input = sys.stdin.readline

num = int(input())
l = []
for _ in range(num):
    l.append(int(input()))

gl = []
for i in range(num-1):
    gl.append(l[i+1] - l[i])

gcd_gl = gl[0]

for i in range(1,num-1):
    gcd_gl = math.gcd(gcd_gl,gl[i])

ans = set([])
for k in range(2,int(gcd_gl**0.5)+1):
    if gcd_gl%k == 0:
        ans.add(k)
        ans.add(gcd_gl//k)
    
if len(ans)>=1:
    ans = list(ans)
    ans.sort()
    print(*ans,end=' ')
print(gcd_gl)