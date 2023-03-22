l = list(map(int,input().split()))
l.sort()
if l[0]+l[1]>l[2]:
    print(l[0]+l[1]+l[2])
else:
    print(2*l[0]+2*l[1]-1)