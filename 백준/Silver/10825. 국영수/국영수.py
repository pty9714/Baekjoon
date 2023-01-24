import sys
input = sys.stdin.readline
a = int(input())
k = []
for i in range(a):
    l = list(input().split())
    for i in range(1,4):
        l[i] = int(l[i])
    k.append(l)
k = sorted(k, key = lambda x : (-x[1], x[2],-x[3],x[0]))
for j in k:
    print(j[0])