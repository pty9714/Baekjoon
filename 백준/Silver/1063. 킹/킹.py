import sys
input= sys.stdin.readline
M = { 'R':(1,0), 'L':(-1,0), 'B':(0,1), 'T':(0,-1)}
king, stone, move = input().split()

a1,b1 = king
kx = ord(a1)-ord('A')
ky = 8-int(b1)

a2,b2 = stone
sx = ord(a2)-ord('A')
sy = 8-int(b2)

for _ in range(int(move)):
  dir = input().rstrip()
  dx = 0
  dy = 0
  for i in dir:
    v,w = M[i]
    dx +=v
    dy +=w
  if 0<=kx+dx<=7 and 0<=ky+dy<=7:
    kx = kx+dx
    ky = ky+dy
    if sx == kx and sy == ky:
      if 0<=sx+dx<=7 and 0<=sy+dy<=7:
        sx = sx+dx
        sy = sy+dy
      else:
        kx = kx-dx
        ky = ky-dy
  else:
    continue   

a1 = chr(kx+ord('A'))
b1 = 8-ky
a2 = chr(sx+ord('A'))
b2 = 8-sy
print(a1+str(b1))
print(a2+str(b2))