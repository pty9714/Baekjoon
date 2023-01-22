import math
a= int(input())
m=0
y=0
l = list(map(int,input().split()))

for j in l:
    y +=math.ceil((j+0.1)/30)*10
    m +=math.ceil((j+0.1)/60)*15

if y>m:
    print('M',m)
elif m>y:
    print('Y',y)
else:
    print('Y','M',m)