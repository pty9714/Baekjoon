
import sys
input = sys.stdin.readline
a = int(input())
L = []
for i in range(a):
    L.append(int(input()))    

L.sort()
print(*L)