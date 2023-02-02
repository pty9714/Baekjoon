stack = []
upr = []
num = int(input())
l = list(map(int,input().split()))
a = l[0]
b = 0
for i in range(1,len(l)):
    if b == 0:
        if a<l[i]:
            b = l[i]
        else:
            a = l[i]
    else:
        if b>=l[i]:
            upr.append(b-a)
            a = l[i]
            b = 0
        elif b<l[i]:
            b = l[i]
            
if b-a>0:
    upr.append(b-a)
try: print(max(upr))
except: print(0)