import sys
input = sys.stdin.readline
a = int(input())
l = list(map(int,input().split()))
l = sorted(l)
total = 0
for i in range(a):
    total += l[i]*(2*i-2*(a-i-1))
print(total)