import sys
input = sys.stdin.readline
a, b = map(int,input().split())
l = set()
m = set()
for i in range(a):
    l.add(input().rstrip())

for j in range(b):
    k = input().rstrip()
    if k in l:
        m.add(k)

print(len(m))
t = []
t = sorted(m)
for i in t:
    print(i)