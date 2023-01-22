
a = int(input())
x= 100
y= 100
for i in range(a):
    j,k = map(int,input().split())
    if j<k:
        x -=k
    elif j>k:
        y -=j
print(x)
print(y)