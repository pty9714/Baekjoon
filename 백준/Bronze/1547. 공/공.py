import sys
input = sys.stdin.readline
l = [0,1,0,0]
for _ in range(int(input())):
    a,b = map(int,input().split())
    l[a],l[b] = l[b],l[a]
for i in range(len(l)):
    if l[i] == 1:
        print(i)