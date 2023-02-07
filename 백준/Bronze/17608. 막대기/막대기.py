import sys
input = sys.stdin.readline
a = int(input())
l = []
for _ in range(a):
    l.append(int(input()))

stick = 0
total = 0
for i in range(a-1,-1,-1):
    if stick<l[i]:
        stick = l[i]
        total +=1

print(total)