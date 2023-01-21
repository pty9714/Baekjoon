import math
d = {}
for i in input():
    if i == '6' or i== '9':
        d['6'] = d.get('6',0) + 1/2
    else:
        d[i] = d.get(i,0) + 1
a=0
for x,y in d.items():
    if y>a:
        a = y

print(math.ceil(a))
