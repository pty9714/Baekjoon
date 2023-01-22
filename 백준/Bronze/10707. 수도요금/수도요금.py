a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
k = 0
if p>=c:
    k+=b
    k+=(p-c)*d
else:
    k = b
print(min([a*p,k]))