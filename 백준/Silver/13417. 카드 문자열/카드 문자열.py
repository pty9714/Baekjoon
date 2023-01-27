import sys
from collections import deque
input = sys.stdin.readline  
tc = int(input())
for _ in range(tc):
    num = int(input())
    l = deque((input().split()))
    t = l[0]
    l.popleft()
    while len(l)>=1:
        if ord(t[0]) >=ord(l[0]):
            t = l.popleft() + t
        else:
            t = t + l.popleft()
    print(t)
