a,b = map(int,input().split())
g = set([])
for i in range(1,int(a**(1/2))+1):
    if a%i == 0:
        g.add(a//i)
        g.add(i)

gl = list(g)
gl.sort()
try: 
    print(gl[b-1])
except:
    print(0)