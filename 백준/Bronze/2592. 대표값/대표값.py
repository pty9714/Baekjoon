import sys
input = sys.stdin.readline
k = {}
total = 0
for _ in range(10):
    a = int(input())
    total +=a
    k[a] = k.get(a,0)+1

l = list(k.items())
l = sorted(l,key = lambda x : -x[1])
print(int(total/10))
print(l[0][0])