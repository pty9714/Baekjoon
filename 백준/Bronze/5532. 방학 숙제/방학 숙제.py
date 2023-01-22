import math
day = int(input())
a = int(input())
b = int(input())
x = int(input())
y = int(input())

kor = math.ceil(a/x)
mat = math.ceil(b/y)
if kor>=mat:
    print(day-kor)
else:
    print(day-mat)