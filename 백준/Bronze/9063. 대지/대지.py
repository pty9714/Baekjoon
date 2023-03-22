n = int(input())
x = []
y = []

for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

if n == 1:
    print(0)
if n>=2:
    print((max(x)-min(x))*(max(y)-min(y)))