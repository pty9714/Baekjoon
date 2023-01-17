a = int(input())
X = []
Y = []
total = 0
for i in range(a):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
for i in range(a):
    total += X[i]*Y[(i+1)%a] - X[(i+1)%a]*Y[i]
total = abs(total)/2
print (total)