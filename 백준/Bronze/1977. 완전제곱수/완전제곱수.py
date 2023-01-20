import math
a = int(input())
b = int(input())
l = []
for i in range(math.ceil(a**(1/2)),int(b**(1/2))+1):
    l.append(i**2)
if l:
    print(sum(l))
    print(l[0])

else:
    print('-1')